# Assume a standard co-ordinate grid where
# the bottom-left corner is (0, 0), and
# co-ordinates increase as you go up or
# right.
#
# If you take a step `up` then your x
# co-ordinate doesn't change, and your y
# co-ordinate increases by 1, therefore:
# UP = (0, 1)

# # Similarly:
# DOWN = (0, -1)
# LEFT = (-1, 0)
# RIGHT = (1, 0)
# DIAGONALLY_UP_LEFT = (-1,1)
# DIAGONALLY_UP_RIGHT = (1,1)
# DIAGONALLY_DOWN_LEFT = (-1,-1)
# DIAGONALLY_DOWN_RIGHT = (1,-1)

directions = {
    "UP": (0,1),
    "DOWN": (0, -1),
    "LEFT": (-1, 0),
    "RIGHT": (1, 0),
    "DIAGONALLY_UP_LEFT": (-1,1),
    "DIAGONALLY_UP_RIGHT": (1,1),
    "DIAGONALLY_DOWN_LEFT": (-1,-1),
    "DIAGONALLY_DOWN_RIGHT": (1,-1),
}

bodyParts = {
    "HEAD": 1,
    "BODY": 2,
    "TAIL": 3,
}


class Snake:
    
    # Create snake with initial body and direction
    # Snake body goes from [tail, ..., head]
    #
    # body: list
    # direction: string
    def __init__(self, body, direction):
    
        # body
        if not isinstance(body, list):
            raise TypeError("Body must be of type list")
        else:
            self.body = body
        
        # direction
        if direction not in directions:
            raise Exception("Direction does not exist")
        else:
            self.direction = direction
        
        # alive
        self.alive = True
    
    
    # Moves snake in a given direction
    # Returns 0 on success
    # Returns -1 on error (i.e. if invalid direction)
    #
    # dir: string
    def take_step(self, dir):
        try:
            self.set_direction(dir)
            direction = directions[dir]
        except Exception as e:
            print("Exception: ",e)
            return -1
    
        # create tuple for new position of head
        new_head = (self.body[0][0] + direction[0], self.body[0][1] + direction[1])
        # print("head = " + str(self.body[0]))
        # print("new head = " + str(new_head))
        
        # insert new position at front of list
        self.body.append(new_head)
        
        # remove tail
        del self.body[0]
        
        return 0
        
    # Set snake's current direction
    #
    # new_direction: string
    def set_direction(self, new_direction):
        if new_direction in directions:
            self.direction = new_direction
        else:
            raise Exception("Invalid direction")
        return 0
            
    # Returns position of snake's head
    def head(self):
        return self.body[0]
    
    def isAlive(self):
        return self.alive
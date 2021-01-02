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
            # new_head = (old_headX + directionX, old_headY + directionY)
        new_head = (self.head()[0] + direction[0], self.head()[1] + direction[1])
        
        # remove tail
        del self.body[0]
        
        # insert new head
        self.body.append(new_head)
        

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
        return self.body[len(self.body) - 1]
    
    # Checks if head has collided with any part of its body
    def hasCollision(self):
        head = self.head()
        
        for part in self.body[:-1]:
            if head[0] == part[0] and head[1] == part[1]:
                return 1
    
        return 0
    
    # Checks if snake occupies a given location (x,y)
    # Returns
    #   1 if snake occupies the space
    #   0 otherwise
    def occupies(self, x, y):
        for part in self.body:
            if part[0] == x and part[1] == y:
                return 1
                
        return 0

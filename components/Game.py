from components.Snake import *

# All coordinates in format [x,y]

class Game:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [0 * width] * height
        # self.snake = Snake([[0,0],[0,1],[0,2],[1,2]],"RIGHT")
        self.snake = Snake([[0,0],[1,0],[2,0],[2,1],[2,2]],"RIGHT")
    
    # Returns matrix with snake added to board
    def board_matrix(self):
        print("printing boar matrix =============")
        
        board = [ [None for i in range(self.width) ] for j in range(self.height)]
        
        s = self.snake
        
        head = (0,0)
        for section in s.body:
            board[len(board) - section[1] - 1][section[0]] = bodyParts["BODY"]
            # board[section[1]][section[0]] = bodyParts["BODY"]
            head = section
        
        # h,w
        board[len(board) - head[1] - 1][head[0]] = bodyParts["HEAD"]
        # board[head[1]][head[0]] = bodyParts["HEAD"]
        
        return board
        
        
    # Render and print current board to console
    def render(self):
        print("Height = " +str(self.height))
        print("Width = " + str(self.width))
        
        
        board = self.board_matrix()
        print("+"+"-"*(len(board[0]))+"+")
        for row in board:
            print("|",end="")
            for val in row:
                if (val == None):
                    print(" ",end="")
                else:
                    if val == bodyParts["BODY"]:
                        print("O",end="")
                    elif val == bodyParts["HEAD"]:
                        print("X",end="")
                    else:
                        print(" ",end="")

            print("|",end="\n")
            
        print("+"+"-"*(len(board[0]))+"+")
        return 0
        
        
    def isOver(self):
    
        # define head variables
        head = self.snake.head()
        headX = head[0]
        headY = head[1]
    
        # check if head is within bounds
        if (headX < 0 or headX >= self.width or headY < 0 or headY >= self.height):
            return 1
    
        # check if head hit any part of body
        return self.snake.hasCollision()
    
    
    def move(self, direction):
        return self.snake.take_step(direction)
            
            
    
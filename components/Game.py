from Snake import *

# All coordinates in format [w,h]

class Game:
    
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.board = [[None] * width] * height
        self.snake = Snake([[0,0],[0,1],[0,2],[1,2]],"RIGHT")
    
    
    # Render and print current board to console
    # TODO: render snake
    def render(self):
        print("Height = " +str(self.height))
        print("Width = " + str(self.width))
        
        print("+"+"-"*(self.width)+"+")
        for row in self.board:
            print("|",end="")
            for val in row:
                if (val != None):
                    print(val,end="")
                else:
                    print(" ",end="")
            print("|",end="\n")
            
        print("+"+"-"*(self.width)+"+")
        
        
        
    
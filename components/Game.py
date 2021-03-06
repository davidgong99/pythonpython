from components.Snake import *
import random


pieces = {
    "HEAD": 1,
    "BODY": 2,
    "TAIL": 3,
    "APPLE": 4,
}

# All coordinates in format [x,y]

class Game:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [0 * width] * height
        self.snake = Snake([[2,2]],"RIGHT")
        self.apple = (3,3)
        self.score = 0
        self.maxScore = self.height * self.width - self.snake.length()
    
    # Returns matrix with snake added to board
    def board_matrix(self):
        # print("printing boar matrix =============")
        
        board = [ [None for i in range(self.width) ] for j in range(self.height)]
        
        s = self.snake
        
        head = (0,0)
        for section in s.body:
            board[len(board) - section[1] - 1][section[0]] = pieces["BODY"]
            # board[section[1]][section[0]] = pieces["BODY"]
            head = section
        
        # h,w
        board[len(board) - head[1] - 1][head[0]] = pieces["HEAD"]
        # board[head[1]][head[0]] = pieces["HEAD"]
        
        # insert apple
        board[len(board) - self.apple[1] - 1][self.apple[0]] = pieces["APPLE"]
        
        return board
        
        
    # Render and print current board to console
    def render(self):
        print("**************\n* Score = ",self.score,"*\n**************")

        board = self.board_matrix()
        print("+"+"-"*(len(board[0]))+"+")
        for row in board:
            print("|",end="")
            for val in row:
                if (val == None):
                    print(" ",end="")
                else:
                    if val == pieces["BODY"]:
                        print("O",end="")
                    elif val == pieces["HEAD"]:
                        print("X",end="")
                    elif val == pieces["APPLE"]:
                        print("A",end="")
                    else:
                        print(" ",end="")

            print("|",end="\n")
            
        print("+"+"-"*(len(board[0]))+"+")
        return 0
        
    # Check if game is over
    # Returns
    #   1 if game is over
    #   0 otherwise
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
    
    # Move snake in given direction
    #
    # direction: string
    def move(self, direction):
        # move snake
        if self.snake.take_step(direction) == -1:
            return -1 # invalid key
    
        # if snake moved into apple, generate new one
        if self.snake.head() == self.apple:
            self.snake.extend()
            self.incrementScore()
            self.generateApple()
    
        if self.score == self.maxScore:
            return 2 # congratulations
            
        if self.isOver():
            return -2 # game over
            
        return 0
            
    # Generates a random coordinate for the apple
    # Store in self.apple as a tuple (appleX, appleY)
    # The apple will not be in a space occupied by the snake
    def generateApple(self):
        if self.score == self.maxScore:
            return 0
        appleFound = False
        
        while (not appleFound):
            appleX = random.randrange(self.width)
            appleY = random.randrange(self.height)
            
            if not self.spaceOccupied(appleX, appleY):
                self.apple = (appleX, appleY)
                appleFound = True
            
    
    # Checks if a given location on the game board is occupied
    def spaceOccupied(self, x, y):
        return self.snake.occupies(x,y)
        
    def incrementScore(self):
        self.score += 1
    
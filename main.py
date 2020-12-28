from components.Game import Game
from components.Apple import Apple



g = Game(5,4)

g.render()


while not g.isOver():
    inputKey = input("Enter move (w,a,s,d): ")
    print(inputKey)
    
    # TODO: check if valid key, and handle input


from components.Game import Game
from components.Apple import Apple

g = Game(5,4)

while not g.isOver():
    g.render()
    inputKey = input("Enter move (w,a,s,d,x): ")

    ret = 0
    
    if (inputKey == "x"): # exit
        print("Exiting")
        break
    elif inputKey == "w": # up
        print("UP")
        ret = g.move("UP")
    elif inputKey == "a": # left
        print("LEFT")
        ret = g.move("LEFT")
    elif inputKey == "s": # down
        print("DOWN")
        ret = g.move("DOWN")
    elif inputKey == "d": # right
        print("RIGHT")
        ret = g.move("RIGHT")
    else: # invalid key
        print("Invalid key")
        
    if ret == -1:
        # print("Invalid key")
        print("Invalid key")
        break
    if ret == -2:
        print("Game over")
        break
    if ret == 2:
        print("Congratulations!")
        break

g.render()
print("Final score = ",g.score)
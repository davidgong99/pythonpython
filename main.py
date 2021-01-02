from components.Game import Game
from components.Apple import Apple
import sys

if len(sys.argv) != 3:
    print("Usage: python main.py <width> <height>")
    exit()

try:
    width = int(sys.argv[1])
    height = int(sys.argv[2])
except Exception as e:
    print("Exception: ",e)


g = Game(width, height)

while True:
    g.render()
    inputKey = input("Enter move (w,a,s,d,x): ")

    ret = 0
    
    if (inputKey == "x"): # exit
        print("Exiting")
        break
    elif inputKey == "w": # up
        # print("UP")
        ret = g.move("UP")
    elif inputKey == "a": # left
        # print("LEFT")
        ret = g.move("LEFT")
    elif inputKey == "s": # down
        # print("DOWN")
        ret = g.move("DOWN")
    elif inputKey == "d": # right
        # print("RIGHT")
        ret = g.move("RIGHT")
    else: # invalid key
        print("Invalid key")
        
    if ret == -1:
        print("Invalid key")
        break
    if ret == -2:
        print("Game over")
        break
    if ret == 2:
        g.render()
        print("Congratulations!")
        
        break

# g.render()
print("Final score = ",g.score)
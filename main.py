from components.Game import Game
from components.Apple import Apple



g = Game(5,4)


# g.initialize(5,4)
g.render()

# s = Snake([(1,1),(2,1),(3,1)], directions["UP"])
print("body = ",s.body)
print("dirction = ",s.direction)

s.take_step("UP")
s.take_step("RIGHT")

try:
    s.take_step("sadsa")
except Exception as e:
    print("Exception: ",e)
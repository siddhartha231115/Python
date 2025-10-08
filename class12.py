"""import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(400,400)
polygon=turtle.Turtle()
numside = 6
sidelen = 70
angle = 360.0 / numside
for i in range(numside):
    polygon.forward(sidelen)
    polygon.right(angle)
turtle.done()"""

"""import turtle
turtle.Screen().bgcolor("cyan")
board = turtle.Turtle()
board.forward(100)
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)
board.penup()
board.right(150)
board.forward(50)
board.pendown()
board.right(90)
board.forward(100)
board.right(120)
board.forward(100)
board.right(120)
board.forward(100)
turtle.done()"""

import turtle
mywn = turtle.Screen
mypen = turtle.Turtle()
size = 0 
while True:
    for i in range(4):
        mypen.fd(size + 1)
        mypen.left(90)
        size = size-5
    size= size+1
    turtle.done()
'''
turtle colours: https://cs111.wellesley.edu/reference/colors
colour rgb codes: https://trinket.io/docs/colors
turtle graphics documentation: https://docs.python.org/3/library/turtle.html

'''

from turtle import Turtle, Screen

joce = Turtle()
joce.shape("turtle")
# change turtle fill colour
# can use hex codes (#00CED1), colour names ("blue")
joce.color("#00CED1")
# Change colour of the line the turtle leaves behind it
joce.pencolor("red")

# draw a square
for _ in range(4):
    joce.forward(100)
    joce.right(90)

# draw a dashed line
joce.right(180)
for _ in range(10):
    joce.forward(10)
    joce.penup()
    joce.forward(10)
    joce.pendown()






# these need to be at the bottom of the file after the turtle does everything it needs to do
# use documentation to see why
screen = Screen()
screen.exitonclick()

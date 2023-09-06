'''
turtle colours: https://cs111.wellesley.edu/reference/colors
colour rgb codes: https://trinket.io/docs/colors
turtle graphics documentation: https://docs.python.org/3/library/turtle.html

'''

import random
from turtle import Turtle, Screen
# can import everything by using - from turtle import *
# can also alias modules - import turtle as t
# can now write - joce = t.Turtle()

# some modules need to be installed first before importing

screen = Screen()
# colormode of the screen to 255 allows the (r,g,b) value to be used when changing colour
screen.colormode(255)

joce = Turtle()
joce.shape("turtle")
# change turtle fill colour
# can use hex codes (#00CED1), colour names ("blue")
joce.color("#00CED1")
# Change colour of the line the turtle leaves behind it
joce.pencolor("red")

# # draw a square
# for _ in range(4):
#     joce.forward(100)
#     joce.right(90)

# # draw a dashed line
# joce.right(180)
# for _ in range(10):
#     joce.forward(10)
#     joce.penup()
#     joce.forward(10)
#     joce.pendown()

# # draw shapes with 3 sides up to 10 sides in sequence, all with 100 length sides and different random colours per shape
def change_colour(turt):
    '''Change the input turtle to a random colour. Retrun the new coloured turtle.'''
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)

    turt.pencolor((R, G, B))
    return turt

# for sides in range(3, 11):
#     joce = change_colour(joce)
#     for _ in range(sides):
#         joce.forward(100)
#         joce.right(360 / sides)

# generate a random walk - turtle makes random moves in N/S/E/W direction
# turtle always moves the same distance, then randomly picks a new direction.
# colour of line changes every time the turtle moves.

def pick_direction():
    '''Randomly return a random direction.'''
    return random.choice([0,90,180,270])

joce.pensize(11)
joce.speed(10)

for _ in range(200):
    joce = change_colour(joce)
    direction = pick_direction()
    joce.setheading(direction)
    joce.forward(25)


# these need to be at the bottom of the file after the turtle does everything it needs to do
# use documentation to see why
screen.exitonclick()

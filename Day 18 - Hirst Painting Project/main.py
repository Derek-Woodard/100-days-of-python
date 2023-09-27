'''Use the turtle module to paint a Hirst dot painting.'''
import random
from turtle import Turtle, Screen
# import colorgram


# colorgram info found here: https://pypi.org/project/colorgram.py/

# Below is used to extract and create a list of colours
# for simplicity, that list is copied and made into a list.
# # extract colours from the image
# extracted_colours = colorgram.extract("Day 18 - Hirst Painting Prokect/Hirst_image.jpg", 30)

# colours = []

# # extract the R,G,B values from each colour, and create a new colour object
# for colour in extracted_colours:
#     R = colour.rgb.r
#     G = colour.rgb.g
#     B = colour.rgb.b
#     colours.append((R,G,B))

# print(colours)

# white shades are removed
colours = [(44, 95, 148), (179, 46, 75), (227, 208, 100), (209, 156, 88), (179, 169, 33),
            (137, 88, 63), (115, 179, 209), (201, 74, 121), (214, 130, 174), (229, 70, 50),
            (90, 104, 191), (46, 166, 119), (27, 146, 84), (122, 218, 208), (52, 56, 93),
            (121, 43, 71), (119, 47, 36), (35, 183, 194), (227, 170, 189), (128, 185, 162),
            (174, 186, 220), (156, 206, 217), (234, 171, 162), (51, 54, 70), (211, 209, 39),
            (87, 43, 32)]

def set_colour(turtle):
    '''Change the input turtle to a random colour from the selection. 
    Return the new coloured turtle.'''
    colour = random.choice(colours)
    turtle.color(colour)
    return turtle

turt = Turtle()
screen = Screen()
screen.colormode(255)
turt.speed(0)

CIRCLE_RADIUS = 20
CIRCLE_GAP = 50
CIRCLES_UP = 10
CIRCLES_SIDE = 10
SCREEN_X = (CIRCLE_RADIUS * CIRCLES_UP) + (CIRCLE_GAP * (CIRCLES_UP) - CIRCLE_RADIUS)
SCREEN_Y = (CIRCLE_RADIUS * CIRCLES_SIDE) + (CIRCLE_GAP * (CIRCLES_SIDE) - CIRCLE_RADIUS)

screen.setup(SCREEN_X, SCREEN_Y)

turt.penup()
turt.setpos(-(SCREEN_X / 2), (SCREEN_Y / 2) - CIRCLE_RADIUS)
turt.setheading(270)

for _ in range(CIRCLES_SIDE):
    for _ in range(CIRCLES_UP):
        turt.pendown()
        turt = set_colour(turt)
        # can also use turle.dot(radius,colour) to make the dots
        turt.begin_fill()
        turt.circle(CIRCLE_RADIUS)
        turt.end_fill()
        turt.penup()

        turt.forward(CIRCLE_GAP + CIRCLE_RADIUS)

    turt.setheading(90)
    turt.forward((CIRCLE_GAP + CIRCLE_RADIUS) * CIRCLES_UP)
    turt.setheading(0)
    turt.forward(CIRCLE_GAP + CIRCLE_RADIUS)
    turt.setheading(270)


screen.exitonclick()

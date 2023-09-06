
import random
from turtle import Turtle, Screen
import colorgram


# colorgram info found here: https://pypi.org/project/colorgram.py/

# Below is used to extract and create a list of colours - for simplicity, that list is copied and made into a list.
# # extract colours from the image
# extracted_colours = colorgram.extract("Hirst_image.jpg", 30)

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

#TODO make a painting with 10 x 10 rows of dots
#TODO the dots are about 20 pixels radius and spaced 50 apart


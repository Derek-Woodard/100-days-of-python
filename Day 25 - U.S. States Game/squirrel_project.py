'''
create a csv calle squirrel_count.csv
this file only contains the fur colour of the squirrels, and the number found
'''

import pandas

data = pandas.read_csv("Day 25 - U.S. States Game/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colour_data = data["Primary Fur Color"]
red_data = colour_data[data["Primary Fur Color"] == "Cinnamon"]
grey_data = colour_data[data["Primary Fur Color"] == "Gray"]
black_data = colour_data[data["Primary Fur Color"] == "Black"]

red_count = red_data.count()
grey_count = grey_data.count()
black_count = black_data.count()

squirrel_count = {
    "Fur Colour": ["Cinnamon", "Gray", "Black"],
    "Count": [red_count, grey_count, black_count]
}

squirrel_data = pandas.DataFrame(squirrel_count)
squirrel_data.to_csv('Day 25 - U.S. States Game/Squirrel_Count.csv')

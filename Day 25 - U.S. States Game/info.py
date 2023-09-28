'''
working with Pandas library to use csv data files
csv - Comma Separated Values

can import csv library
can use csv.read(data file name) to create a reader object
reader objects can be looped through with for loops
each iteration of the loop covers a single row from teh data file

using csv takes a lot of maneuvering to work with
note how much it takes to just get a list of temperatures from a column below
so we use the Pandas module instead

websites with info in pandas
https://pandas.pydata.org/docs/
https://pandas.pydata.org/docs/reference/index.html

with pandas, can use pandas.read_csv(file path) to get csv data
printing the data will format it really well
you can then use that variable name with square brackets to get columns
data = pandas.read_csv('Day 25 - U.S. States Game/weather_data.csv')
print(data['temp'])

note the difference between pandas and csv
'''

# # old method of extracting data - not useful for csv
# with open('Day 25 - U.S. States Game/weather_data.csv') as weather_data:
#     data = weather_data.readlines()

# for row in data:
#     row = row.strip()
#     print(row)

# import csv

# with open('Day 25 - U.S. States Game/weather_data.csv') as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv('Day 25 - U.S. States Game/weather_data.csv')
# print(data['temp'])

'''
can use type method to see what type the data is from the pandas
from below, you can see that it is a pandas.core.frame.DataFrame

If you check on the type of one column, the type is different
it is a pandas.core.series.Series

these two concepts are important
the whole table is a data frame
the series is a list that is a single column from the data

data frames can be converted into many things, including excel files, and dictionaries
can also convert into lists
'''

# print(type(data))
# print(type(data['temp']))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# print(temp_list)

# to find average temperature from weather_data normally
# temp_list = data['temp'].to_list()
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)

# there is a mean method in pandas that does the same thing faster
# print(data['temp'].mean())

# get the max temp value using data series methods
# print(data['temp'].max())

# alternative way to using the ["column name"]
# pandas converts the column headings into attributes of the file
# For our data csv file, we can use data.conditions to get the conditions series
# note that capitilization is important for both ["Name"] and the attribute
# print(data.condition)

# getting rows
# get whole table, then get the columnn you want to search through
# with the column selected, use == to find the specific row name from that column
# print(data[data.day == "Monday"])

# pull the row out for the day with the max temperature
# print(data[data.temp == data.temp.max()])
# can go one step further by tapping into the row
# monday = data[data.day == "Monday"]
# print(monday.condition)

# get mondays temp, and convert it into farenheit
# monday = data[data.day == "Monday"]
# print((1.8 * monday.temp) + 32)

# create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# # can even write csv files by converting a dataframe into a csv
# data.to_csv('Day 25 - U.S. States Game/new_data.csv')

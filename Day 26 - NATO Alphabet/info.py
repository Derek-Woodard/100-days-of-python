'''
Lists and Dictionary comprehension
Aim to make a console program where you enter a word in console
That word is then returned as a list giving the NATO words for each letter

list comprehension - unique to python
create a new list from a prev list

ex.
you have a list with three numbers in it.
you want to make a new list that adds 1 to the value of the numbers in the first list
code:
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

using list comprehension this can be made into one line
the following shows list comprehension:
new_list = [new_item for item in list]

for the above ex using list comprehension:
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
'''

numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]
# print(new_numbers)

# working with a string
NAME = 'Derek'
# takes each letter in a string and adds it into the list
letters_list = [letter for letter in NAME]
# print(letters_list)

# challenge:
# create a range from 1-5 using range(1,5) that doubles the values:
range_list = [number * 2 for number in range(1,5)]
# print(range_list)

# conditional list comprehension: new_list = [n + 1 for n in numbers if test]
# if test allows us to only add new_item if test passes
# ex:
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# make a new list that only has the names with 4 or fewer letters
short_names = [name for name in names if len(name) < 5]
# print(short_names)

# challenge
# take above list of names and any name with 5+ letters gets turned into the upper case version
long_names = [name.upper() for name in names if len(name) > 4]
# print(long_names)

# exercises:
# Take a list and square all the values in it to form a new list
numbers = [1,1,2,3,4,8,13,21,34,55]
squared_numbers = [num ** 2 for num in numbers]
# print(squared_numbers)

# Take input to form a list of numbers - use list comprehension to convert from string
list_of_strings = input().split(',')
list_of_nums = [int(num_string) for num_string in list_of_strings]
# filter out the odd numbers
list_of_evens = [num for num in list_of_nums if num % 2 == 0]
# print(list_of_evens)

# create a new list covering data overlap between two different lists from text files

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
print(new_numbers)

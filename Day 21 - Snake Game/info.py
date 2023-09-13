'''
inheritance
- classes can inherit
if you make a chef class that can bake, stir and measure
you can make another class - pastry chef
the pastry chef class can be a chef class - inheriting bake, stir and measure,
you can then add in additional things - both attributes and methods

ex.
if you have an Animal class, and want to make a Fish class
class Fish(Animal):
    def __init__(self):
        super().__init__()
        # super will initialize the super class (ie the animal)

if animal has a breathe method, you can adjust it in a sub-class Fish
in Fish, you can do the following:
def breathe(self):
    super().breathe()
    # adjustments can now be made here while mantaining the animal breathe functionality



slicing
- slicing allows you to take smaller sub-lists from a list
ex. if you have a list called piano_keys = [a,b,c,d,e,f,g]
piano_keys[2:5] will be a sublist [c,d,e]
the first number in inclusive, the second number is exclusive
imagine the numbers are between each list item with 0 before the first item

to slice you can use [start:end:jump distance]
if jump distance is negative, you can go backwards

slicing can also be done on tuples
'''

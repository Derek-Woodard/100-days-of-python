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
- 
'''

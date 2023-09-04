
# Making the coffee machine program from day 15 using Object Oriented Programmin (OOP)
# Day 15 was made using procedural programming - working top to bottom, then jumping into a function when needed.
# OOP using a modular approach
# OOP uses classes and objects - the main program manages the overall process
# the classes and objects take care of all the details
# ex. imagine a restaurant - you need a waiter that can be holding plates and has tables they are responsible for (what they have - attributes (variables))
# the water can take orders and payments (what they do - methods (functions))
# in order to take a payment in the restaurant, you need a waiter object
# objects have things (attributes) and do things (methods)
# You can have multiple instances of objects (more than one waiter in the restaurant)
# The waiter is a 'class' that allows you to make waiter objects - the blueprint

# to make a new objects from a class:
# object = Class()
# waiter = WaiterBlueprint()

# Can use packages in python which contain files others have made with a purpose
# to find packages - https://pypi.org/
# example - prettytable - https://pypi.org/project/prettytable/
# packages need to be installed - for prettytables type the following into the terminal on VScode
# pip install prettytable
# 

# Turtle starting code
from turtle import Turtle, Screen

# joel is an object made into the class: Turtle
joel = Turtle()
# From the turtle graphics library you can change the shape of the turtle: https://docs.python.org/3/library/turtle.html
joel.shape("turtle")
joel.color("coral")
joel.forward(100)

# The screen is part of turtle representing the screen the turtle appears on
my_screen = Screen()
# print(my_screen.canvheight)

# joel has attributes that can be accessed
# to access them, use joel.attribute

# This function allows the program to continue running until the user clicks on the screen
my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
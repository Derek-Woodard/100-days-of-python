'''a class for the food the snake is trying to eat'''
from turtle import Turtle

class Food(Turtle):
    '''the food class will be a turtle object'''
    def __init__(self):
        super().__init__()
        self.food = Turtle("circle")

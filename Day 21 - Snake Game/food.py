'''a class for the food the snake is trying to eat'''
from turtle import Turtle
import random

class Food(Turtle):
    '''the food class will be a turtle object'''
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("blue")
        self.speed(0)
        self.refresh()

    def refresh(self):
        '''move the food to a random location'''
        self.goto(random.randint(-280,280), random.randint(-280,280))
        
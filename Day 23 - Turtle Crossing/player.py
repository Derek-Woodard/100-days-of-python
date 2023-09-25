'''the player in the turtle crossing game'''
from turtle import Turtle

STARTING_POSITION = (0, -200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    '''the player turtle class'''
    def __init__(self):
        super().__init__('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_forward(self):
        '''move the player forwards'''
        self.forward(MOVE_DISTANCE)

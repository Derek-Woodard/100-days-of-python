'''a class representing the ball'''

from turtle import Turtle

class Ball:
    '''a turtle that is the ball'''
    def __init__(self):
        self.ball = Turtle('square')
        self.ball.penup()
        self.ball.color('white')

        self.x_direction = 5
        self.y_direction = 5

        self.x_location = 0
        self.y_location = 0

        self.angle = 70


    def move_ball(self):
        '''move the ball'''
        self.x_location += self.x_direction
        self.y_location += self.y_direction
        self.ball.goto(self.x_location, self.y_location)


    def wall_bounce(self):
        '''bounce the ball, reversing the vertical direction'''
        self.y_direction = -self.y_direction

    def paddle_bounce(self):
        '''bounce the ball, reversing the horizontal direction'''
        self.x_direction = -self.x_direction
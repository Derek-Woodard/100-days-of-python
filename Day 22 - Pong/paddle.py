'''A class representing the two player paddles'''

from turtle import Turtle

class Paddle():
    '''represent the player paddle as a turtle'''
    def __init__(self, player_num, x_cor):
        self.player = player_num
        self.paddle = Turtle('square')
        self.paddle.shapesize(0.5, 5)
        self.paddle.setheading(90)

        self.paddle.penup()
        self.paddle.color('white')
        self.paddle.goto(x_cor,0)

    def move_up(self):
        '''move the paddle up'''
        self.paddle.forward(10)

    def move_down(self):
        '''move the paddle down'''
        self.paddle.backward(10)
        
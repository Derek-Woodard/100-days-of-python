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

        self.y_top = 50
        self.y_bottom = -50

    def move_up(self):
        '''move the paddle up'''
        if self.paddle.ycor() < 300:
            self.paddle.forward(10)
            self.y_top += 10
            self.y_bottom += 10

    def move_down(self):
        '''move the paddle down'''
        if self.paddle.ycor() > -290:
            self.paddle.backward(10)
            self.y_top -= 10
            self.y_bottom -= 10
        
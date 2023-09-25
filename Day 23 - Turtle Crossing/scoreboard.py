'''The score tracker for the turtle crossing game'''
from turtle import Turtle

FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    '''the score tracker'''
    def __init__(self):
        super().__init__(visible=False)
        
        self.level = 1

        self.penup()
        self.goto(-210,250)
        self.write(f'Level: {self.level}', False, 'center', FONT)

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
        self.show_score()

    def show_score(self):
        '''display the score'''
        self.write(f'Level: {self.level}', False, 'center', FONT)

    def level_up(self):
        '''increase the level'''
        self.level += 1
        self.undo()
        self.show_score()

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

    def game_over(self):
        '''display the final score at game over'''
        end_text = Turtle(visible=False)
        end_text.write(f'Game over! You made it to level {self.level}', False, 'center', ('Courier', 12, 'normal'))

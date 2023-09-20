'''a class representing the scorekeeping'''

from turtle import Turtle

FONT = ("Courier", 50, "normal")
ALLIGN = "center"

class Score(Turtle):
    '''A turtle that shows the score on top of the screen'''
    def __init__(self, player):
        super().__init__(visible=False)
        self.value = 0

        self.penup()
        self.color('white')

        if player == 1:
            self.goto(-70, 280)
        elif player == 2:
            self.goto(70, 280)

        self.draw_score()


    def increase_score(self):
        '''increase the score'''
        self.value += 1
        self.undo()
        self.draw_score()

    def draw_score(self):
        '''draw the score value'''
        self.write(f"{self.value}", False, ALLIGN, FONT)

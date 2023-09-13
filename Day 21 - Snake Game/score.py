'''Use a turtle to display the score for the snake game.'''
from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALLIGN = "center"

class Score(Turtle):
    '''a score keep turtle'''
    def __init__(self):
        super().__init__(visible=False)
        self.score = 0
        self.penup()
        self.pencolor("white")
        self.goto(0, 270)
        self.show_score()

    def increase(self):
        '''increase the current score by 1 when a fruit is eaten.'''
        self.score += 1
        self.undo()
        self.show_score()

    def show_score(self):
        '''display the score.'''
        self.write(f"Score: {self.score}", False, ALLIGN, FONT)

    def game_over(self):
        '''print game over in the center of the screen.'''
        self.goto(0,0)
        self.write("GAME OVER", False, ALLIGN, FONT)
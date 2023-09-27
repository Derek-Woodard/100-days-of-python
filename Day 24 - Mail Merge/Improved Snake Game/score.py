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
        with open('Day 24 - Mail Merge/Improved Snake Game/high_score.txt') as file:
            self.hi_score = int(file.read())
        self.show_score()

    def increase(self):
        '''increase the current score by 1 when a fruit is eaten.'''
        self.score += 1
        self.show_score()

    def show_score(self):
        '''display the score.'''
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.hi_score}", False, ALLIGN, FONT)

    def reset(self):
        '''set the hi-score then restart the game'''
        if self.score > self.hi_score:
            self.hi_score = self.score
            with open('Day 24 - Mail Merge/Improved Snake Game/high_score.txt', mode="w") as file:
                file.write(f"{self.hi_score}")
        self.score = 0
        self.show_score()

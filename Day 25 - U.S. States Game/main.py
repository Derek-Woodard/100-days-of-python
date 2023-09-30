'''The US States game'''

import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.setup(width=750,height=550)
screen.bgpic('Day 25 - U.S. States Game/blank_states_img.gif')
screen.update()

QUIZ_ACTIVE = True

data = pandas.read_csv('Day 25 - U.S. States Game/50_states.csv')
state_list = data.state.to_list()
known_list = []

dot_marker = Turtle(visible=False)
dot_marker.penup()

while len(known_list) < 50 and QUIZ_ACTIVE:
    guess = (turtle.textinput(f"{len(known_list)}/50", "Name any U.S. State - type 'quit' to exit")).title()

    if guess in state_list and guess not in known_list:

        state_row = data[data.state == guess]
        dot_marker.goto(int(state_row.x), int(state_row.y))
        dot_marker.write(f'{guess}',False,'left',("Times New Roman", 8, "normal"))

        known_list.append(guess)

    if guess == "Quit":
        QUIZ_ACTIVE = False



turtle.mainloop()

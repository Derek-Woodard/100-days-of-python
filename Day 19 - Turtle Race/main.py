'''Create a Turtle race
allow the user to choose which they think will win
'''

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500,400)

choice = screen.textinput("Who will win?",
                           "Which turtle do you choose? type: 'red', 'orange', 'yellow', 'green', 'blue', 'purple'").lower()

turtles = []
colours = ['red','orange','yellow','green','blue','purple']

START_Y = 150

for colour in colours:
    new_turtle = Turtle("turtle")
    new_turtle.color(colour)
    new_turtle.setheading(0)
    new_turtle.penup()
    new_turtle.setpos(-240, START_Y)
    turtles.append(new_turtle)
    START_Y -= 60

if choice:
    RACING = True

while RACING:
    for turtle in turtles:
        turtle.forward(random.randint(0,10))
        if turtle.xcor() >= 230:
            winner = turtle.pencolor()
            RACING = False
            if winner == choice:
                print(f"You won! {winner} was the winning turtle!")
            else:
                print(f"You lost. {winner} was the winning turtle.")

screen.exitonclick()

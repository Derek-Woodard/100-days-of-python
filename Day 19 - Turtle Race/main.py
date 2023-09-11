'''Create a Turtle race
allow the user to choose which they think will win
'''

from turtle import Turtle, Screen
import random

speeds = [3,4,5,6,7]

screen = Screen()
screen.setup(500,400)

choice = screen.textinput("Who will win?",
                           "Which turtle do you choose? type: 'red', 'orange', 'yellow', 'green', 'blue', 'purple'").lower()

turtles = []
colours = ['red','orange','yellow','green','blue','purple']


red = Turtle("turtle")
orange = Turtle("turtle")
yellow = Turtle("turtle")
green = Turtle("turtle")
blue = Turtle("turtle")
purple = Turtle("turtle")

turtles.append(red)
turtles.append(orange)
turtles.append(yellow)
turtles.append(green)
turtles.append(blue)
turtles.append(purple)

start_y = 150
for i in range(len(turtles)):
    turtles[i].color(colours[i])
    turtles[i].setheading(0)
    turtles[i].penup()
    turtles[i].setpos(-240, start_y)
    start_y -= 60

racing = True

while racing:
    for i in range(len(turtles)):
        turtles[i].forward(random.choice(speeds))
        if turtles[i].xcor() >= 240:
            winner = i
            racing = False
            break

print(f"The winner was {colours[i]}")
if colours[i] == choice:
    print("Your turtle won!")
else:
    print("Your turtle lost.")

screen.exitonclick()

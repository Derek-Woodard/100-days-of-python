'''
The Pong game created using turtles
'''

#TODO break down the game into steps
#TODO Step 0.5) Set up the screen with the centre line
#TODO Step 1) create a paddle class that displays paddles on the screen
#TODO Step 2) allow user input to move the paddles up/down - not leaving the screen
#TODO Step 3) Create a ball class that can spawn a ball that moves
#TODO Step 4) Give the ball collision with the top/bottom to bounce
#TODO Step 5) Give the ball collision with the left/right to score then respawn
#TODO Step 6) Give the ball collision with the paddles to bounce
#TODO Step 7) Create a scoreboard class that can track/display the score values

import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

SCREEN_W = 900
SCREEN_H = 700

screen = Screen()
screen.setup(SCREEN_W, SCREEN_H)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

player_1 = Paddle(1, -400)
player_2 = Paddle(2, 400)

ball = Ball()

playing = True

lines = Turtle()
lines.color('white')
lines.penup()
lines.goto(0,SCREEN_H/2)
lines.setheading(270)
lines.hideturtle()
lines.pensize(5)

screen.onkeypress(player_1.move_up, 'w')
screen.onkeypress(player_1.move_down, 's')
screen.onkeypress(player_2.move_up, 'Up')
screen.onkeypress(player_2.move_down, 'Down')

screen.onkeypress(ball.wall_bounce, 'b')

for _ in range(20):
    lines.pendown()
    lines.forward(17.5)
    lines.penup()
    lines.forward(17.5)


while playing:
    time.sleep(0.1)
    ball.move_ball()
    screen.update()


screen.exitonclick()

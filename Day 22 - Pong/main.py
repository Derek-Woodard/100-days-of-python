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
from scoreboard import Score

SCREEN_W = 900
SCREEN_H = 700

screen = Screen()
screen.setup(SCREEN_W, SCREEN_H)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

player_1 = Paddle(1, -400)
player_2 = Paddle(2, 400)

score_1 = Score(1)
score_2 = Score(2)

ball = Ball()

PLAYING = True

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


for _ in range(20):
    lines.pendown()
    lines.forward(17.5)
    lines.penup()
    lines.forward(17.5)

screen.update()
screen.tracer(1)

# a check to ensure the ball does not get stuck inside a paddle
BOUNCED = False

while PLAYING:
    # time.sleep(0.051)
    ball.move_ball()

    # check for bounce on upper and lower walls
    if ball.y_location > 338 or ball. y_location < -338:
        ball.wall_bounce()

    # check if ball has crossed the centre line to allow paddle bouncing again
    if ball.x_location > -10 and ball.x_location < 10:
        BOUNCED = False

    # check for ball contact with the left or right wall
    # give point to opposing team and update their score
    if ball.x_location > 440:
        screen.tracer(0)
        ball.respawn()
        score_1.increase_score()
        screen.tracer(1)

    if ball.x_location < -440:
        screen.tracer(0)
        ball.respawn()
        score_2.increase_score()
        screen.tracer(1)

    # check for bounce on collision with paddles
    # right paddle
    if ball.x_location > 380 and ball.x_location < 420:
        if ball.y_location < player_2.y_top + 10 and ball.y_location > player_2.y_bottom - 10:
            if not BOUNCED:
                ball.paddle_bounce()
                BOUNCED = True

    # left paddle
    if ball.x_location < -380 and ball.x_location > -420:
        if ball.y_location < player_1.y_top + 10 and ball.y_location > player_1.y_bottom - 10:
            if not BOUNCED:
                ball.paddle_bounce()
                BOUNCED = True

    # screen.update()


screen.exitonclick()

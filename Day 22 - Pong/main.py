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

from turtle import Screen

screen = Screen()
screen.setup(900, 700)
screen.bgcolor('black')


screen.exitonclick()

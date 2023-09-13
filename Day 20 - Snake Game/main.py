'''Snake game using OOP and the turtle module'''
# break game down into 7 steps - first 3 on day 20, last 4 on day 21
# Step 1: create the snake body - uise 3 squares
# Step 2: move the snake - always moving forward - can change direction
# Step 3: control the snake - use arrow keys
#TODO Step 4: detect collision for food - add food, and make snake grow
#TODO Step 5: create scoreboard - track number of food pieces
#TODO Step 6: detect wall collisions - game over screen
#TODO Step 7: detect collision with tail - game over screen

import time
from turtle import Turtle, Screen
from snake_body import Snake

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake using turtles")
screen.tracer(0)

player = Snake()

screen.listen()
screen.onkeypress(player.turn_up,"Up")
screen.onkeypress(player.turn_right, "Right")
screen.onkeypress(player.turn_down, "Down")
screen.onkeypress(player.turn_left, "Left")

PLAYING = True
TEMP = 0

#while PLAYING:
while TEMP < 100:

    time.sleep(0.1)
    screen.update()
    player.move_snake()
    TEMP += 1

screen.exitonclick()

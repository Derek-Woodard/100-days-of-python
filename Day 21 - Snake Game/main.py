'''Snake game using OOP and the turtle module'''
# break game down into 7 steps - first 3 on day 20, last 4 on day 21
# Step 1: create the snake body - uise 3 squares
# Step 2: move the snake - always moving forward - can change direction
# Step 3: control the snake - use arrow keys
# Step 4: detect collision for food - add food, and make snake grow
# Step 5: create scoreboard - track number of food pieces
#TODO Step 6: detect wall collisions - game over screen
#TODO Step 7: detect collision with tail - game over screen

import time
from turtle import  Screen
from snake_body import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake using turtles")
screen.tracer(0)

player = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkeypress(player.turn_up,"Up")
screen.onkeypress(player.turn_right, "Right")
screen.onkeypress(player.turn_down, "Down")
screen.onkeypress(player.turn_left, "Left")

PLAYING = True

while PLAYING:
    time.sleep(0.1)
    player.move_snake()
    screen.update()

    # detect food collision
    if player.head.distance(food) < 15:
        food.refresh()
        score.increase()
        player.add_segment()

    # detect wall collision
    if player.head.xcor() > 280 or player.head.xcor() < -280 or player.head.ycor() > 280 or player.head.ycor() < -280:
        PLAYING = False

    # detect tail collision
    for i in range(len(player.segments)-1):
        if player.head.distance(player.segments[i+1]) < 19:
            PLAYING = False

score.game_over()

screen.exitonclick()

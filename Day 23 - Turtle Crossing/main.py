'''
essentially frogger but with a turtle and randomly coloured rectangles travelling across the screen
once the turtle reaches the end, the cars speed up and the player resets at the bottom
once the turtle hits a car, it's game over
'''
# make starter screen - 600 x 600, tracer(0), update to refresh
# Make player turtle class - can only move forwards
#TODO Make car class - have speed attribute that moves them from right to left
#TODO when player reaches top, move them to bottom, increase car speed attribute
#TODO spawn in cars on right side at random heights (not at player start height)
#TODO set up game over screen for player/car collision
#TODO give cars random colours
# make scoreboard class to track progress

import time
from random import random
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from cars import Cars

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

level = Scoreboard()

car_manager = Cars()

player = Player()

screen.onkeypress(player.move_forward, 'Up')

PLAYING = True

while PLAYING:
    time.sleep(0.1)

    if player.ycor() > FINISH_LINE_Y:
        player.respawn()
        level.level_up()
        car_manager.increase_speed()

    if random() > 0.9:
        car_manager.add_car()

    car_manager.move_cars()
    # car_manager.remove_car()
    screen.update()

screen.exitonclick()

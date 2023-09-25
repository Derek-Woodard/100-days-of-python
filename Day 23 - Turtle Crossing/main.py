'''
essentially frogger but with a turtle and randomly coloured rectangles travelling across the screen
once the turtle reaches the end, the cars speed up and the player resets at the bottom
once the turtle hits a car, it's game over
'''
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

    for car in car_manager.car_list:
        if abs(player.ycor() - car.ycor()) < 20:
            if player.distance(car) < 40:
                PLAYING = False
                level.game_over()

    screen.update()

screen.exitonclick()

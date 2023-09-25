'''The car manager for the cars in turtle crossing'''
from random import choice
from turtle import Turtle

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SPAWN_RANGE = range(-180, 280, 10)

class Cars():
    '''the manager for all cars and their speeds'''
    def __init__(self):
        self.car_list = []
        self.movement = STARTING_MOVE_DISTANCE
        self.move_increment = MOVE_INCREMENT

    def add_car(self):
        '''add cars to the list'''
        new_car = Turtle('square')
        new_car.penup()
        new_car.color(choice(COLORS))
        new_car.setheading(180)
        new_car.shapesize(1,3)
        new_car.goto(330, choice(SPAWN_RANGE))
        self.car_list.append(new_car)

    # def remove_car(self):
    #     '''ensure no cars off the left of the screen are maintained'''
    #     new_cars = []
    #     for car in self.car_list:
    #         if car.xcor() > -330:
    #             new_cars.append(car)
    #     self.car_list = new_cars

    def move_cars(self):
        '''move all the cars in the list by the increment'''
        for car in self.car_list:
            car.forward(self.movement)
            if car.xcor() < -330:
                self.car_list.remove(car)

    def increase_speed(self):
        '''make the cars move faster'''
        self.movement += self.move_increment

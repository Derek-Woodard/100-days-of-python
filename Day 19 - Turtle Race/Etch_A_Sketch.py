'''Use the turtle module to make an etc-a-sketch'''
from turtle import Turtle, Screen

etch = Turtle()
screen = Screen()

def forward():
    '''move the turtle forwards.'''
    etch.forward(10)

def left():
    '''Turn the turtle left'''
    etch.left(10)

def right():
    '''Turn the turtle right.'''
    etch.right(10)

def back():
    '''move the turtle backwards.'''
    etch.back(10)

def reset():
    '''clear the screen and put restart at the center.'''
    etch.reset()

# note that the function onkey takes another function as input - higher order functions
# the input function has no (), as they call the function
screen.listen()
screen.onkey(forward, 'w')
screen.onkey(left, 'a')
screen.onkey(right, 'd')
screen.onkey(back, 's')
screen.onkey(reset, 'c')

screen.exitonclick()

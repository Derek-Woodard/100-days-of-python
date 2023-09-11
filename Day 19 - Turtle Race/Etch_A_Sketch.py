'''Use the turtle module to make an etc-a-sketch'''
from turtle import Turtle, Screen

etch = Turtle()
screen = Screen()

def forward():
    '''move the turtle forwards.'''
    etch.forward(5)

def left():
    '''Turn the turtle left'''
    etch.left(5)

def right():
    '''Turn the turtle right.'''
    etch.right(5)

def back():
    '''move the turtle backwards.'''
    etch.back(5)

# note that the function onkey takes another function as input
# the input function has no (), as they call the function
screen.listen()
screen.onkey(forward, 'w')
screen.onkey(left, 'a')
screen.onkey(right, 'd')
screen.onkey(back, 's')


screen.exitonclick()

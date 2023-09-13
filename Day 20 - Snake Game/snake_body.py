'''the snake body'''

from turtle import Turtle

class Snake():
    def __init__(self):
        self.segments = []
        for i in range(3):
            segment = Turtle("square")
            segment.color("white")
            self.segments.append(segment)
            segment.setpos(i*-20, 0)

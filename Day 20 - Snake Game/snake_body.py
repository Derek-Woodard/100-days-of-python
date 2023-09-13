'''the snake body'''

from turtle import Turtle

class Snake():
    '''The snake class that tracks the number of segments
    This also tracks the location of each segment
    '''
    def __init__(self):
        self.segments = []
        for i in range(3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            self.segments.append(segment)
            segment.setpos(i*-20, 0)

    def move_snake(self):
        '''move the snake forwards'''
        for seg in reversed(self.segments):
            if self.segments.index(seg) == 0:
                seg.forward(20)
            else:
                new_x = self.segments[self.segments.index(seg) - 1].xcor()
                new_y = self.segments[self.segments.index(seg) - 1].ycor()
                seg.goto(new_x, new_y)

    def turn_up(self):
        '''turn the snake up'''
        self.segments[0].setheading(90)

    def turn_left(self):
        '''turn the snake left'''
        self.segments[0].setheading(180)

    def turn_down(self):
        '''turn the snake down'''
        self.segments[0].setheading(270)

    def turn_right(self):
        '''turn the snake right'''
        self.segments[0].setheading(0)
        
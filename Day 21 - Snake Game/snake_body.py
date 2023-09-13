'''the snake body'''

from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

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
        self.head = self.segments[0]

    def move_snake(self):
        '''move the snake forwards'''
        for seg in reversed(self.segments):
            if self.segments.index(seg) == 0:
                seg.forward(MOVE_DISTANCE)
            else:
                new_x = self.segments[self.segments.index(seg) - 1].xcor()
                new_y = self.segments[self.segments.index(seg) - 1].ycor()
                seg.goto(new_x, new_y)

    def turn_up(self):
        '''turn the snake up'''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_left(self):
        '''turn the snake left'''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_down(self):
        '''turn the snake down'''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_right(self):
        '''turn the snake right'''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self):
        '''add a new segment to the end of the snake.'''
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setpos(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(new_segment)

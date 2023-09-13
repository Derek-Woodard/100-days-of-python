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
        for seg in self.segments:   
            seg.forward(20)

            # if self.segments.index(seg) == 0:
            #     temp_loc = seg.pos()
            #     seg.forward(3)
            # else:
            #     movement = temp_loc - seg.pos()
            #     print(temp_loc)
            #     print(seg.pos())
            #     print(f"{movement} segment {self.segments.index(seg)}")
            #     seg.goto(movement)
            #     temp_loc = seg.pos()
                


    # def turn_snake(self, direction):

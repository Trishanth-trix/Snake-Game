from turtle import Turtle

SNAKE_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.creat_snake()
        self.head=self.segments[0]

    def creat_snake(self):

        for position in SNAKE_POSITION:

            snake1 = Turtle("circle")

            snake1.color("blue")
            snake1.penup()
            snake1.goto(position)
            self.segments.append(snake1)
    def add_segment(self,position):
        new_segment = Turtle("circle")
        new_segment.color("pink")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    def extend(self):
        self.add_segment((self.segments[-1]).position())

    def move(self):

        for seg_index in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_index - 1].xcor()
            y = self.segments[seg_index - 1].ycor()
            self.segments[seg_index].goto(x, y)
        self.segments[0].forward(DISTANCE)
    def reset(self):
        for i in self.segments:
            i.goto(100,1000)
        self.segments.clear()
        self.creat_snake()
        self.head=self.segments[0]
    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def left(self):
        if self.head.heading() !=RIGHT:
            self.segments[0].setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)


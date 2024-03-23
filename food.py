from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.generate_food()

    def generate_food(self):
        rand_x = random.randint(-305, 305)
        rand_y = random.randint(-305, 305)
        self.goto(rand_x, rand_y)



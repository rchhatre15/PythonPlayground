from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("circle")
        self.color("red")
        self.shapesize(.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

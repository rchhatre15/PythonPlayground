from turtle import Turtle
import random


class Obstacle(Turtle):
    def __init__(self):
        super().__init__()
        colors = ["red", "purple", "blue", "green", "orange", "brown"]
        self.color(random.choice(colors))
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=2)
        self.pu()
        self.goto(390, random.randint(-240, 240))
        self.setheading(180)

    def refresh(self):
        if self.ycor() < -380:
            self.hideturtle()
        else:
            self.forward(10)

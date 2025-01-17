from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color("white")
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)

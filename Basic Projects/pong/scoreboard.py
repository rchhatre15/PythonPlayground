from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.right = 0
        self.left = 0
        self.pu()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 260)
        self.hideturtle()
        self.write(f"{self.left}     {self.right}", align="center", font=("Courier", 35, "normal"))

    def increase_right(self):
        self.right += 1
        self.clear()
        self.write(f"{self.left}     {self.right}", align="center", font=("Courier", 35, "normal"))

    def increase_left(self):
        self.left += 1
        self.clear()
        self.write(f"{self.left}     {self.right}", align="center", font=("Courier", 35, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Courier", 35, "normal"))

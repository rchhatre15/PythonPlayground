from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.pu()
        self.color("black")
        self.speed("fastest")
        self.goto(-150, 260)
        self.hideturtle()
        self.write(f"Level: {self.level}", align="right", font=("Courier", 20, "normal"))

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="right", font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Courier", 25, "normal"))

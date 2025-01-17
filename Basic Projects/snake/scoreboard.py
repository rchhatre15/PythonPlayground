from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.pu()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 305)
        self.hideturtle()
        self.increase()

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.high_score}", align="center", font=("Courier", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = -1
        self.increase()

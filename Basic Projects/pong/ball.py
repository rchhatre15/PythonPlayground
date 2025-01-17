from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.refresh()

    def refresh(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce(self, instruction):
        if instruction == "y":
            self.y_move *= -1
        else:
            if self.x_move < 0:
                self.x_move -= 2
            else:
                self.x_move += 2
            self.x_move *= -1

            if self.y_move < 0:
                self.y_move -= 2
            else:
                self.y_move += 2


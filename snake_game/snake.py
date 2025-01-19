from turtle import Turtle


class Snake:
    def __init__(self):
        square_head = Turtle("square")
        square_head.color("white")
        square_head.pu()
        square_second = Turtle("square")
        square_second.color("white")
        square_second.pu()
        square_second.goto(-20, 0)
        square_third = Turtle("square")
        square_third.color("white")
        square_third.pu()
        square_third.goto(-40, 0)

        self.squares = [square_head, square_second, square_third]
        # self.food = None
        # self.generate_food()

    def reset(self):
        for square in self.squares:
            square.goto(1000, 1000)
        self.squares.clear()

        square_head = Turtle("square")
        square_head.color("white")
        square_head.pu()
        square_second = Turtle("square")
        square_second.color("white")
        square_second.pu()
        square_second.goto(-20, 0)
        square_third = Turtle("square")
        square_third.color("white")
        square_third.pu()
        square_third.goto(-40, 0)

        self.squares = [square_head, square_second, square_third]

    def move_up(self):
        if not self.squares[0].heading() == 270:
            self.squares[0].setheading(90)

    def move_right(self):
        if not self.squares[0].heading() == 180:
            self.squares[0].setheading(0)

    def move_left(self):
        if not self.squares[0].heading() == 0:
            self.squares[0].setheading(180)

    def move_down(self):
        if not self.squares[0].heading() == 90:
            self.squares[0].setheading(270)

    def move(self):
        temp_cor = self.squares[0].pos()
        self.squares[0].forward(20)
        for square in self.squares[1:]:
            new_cor = square.pos()
            square.goto(temp_cor)
            temp_cor = new_cor

    def game_on(self):
        return 300 > self.squares[0].xcor() > -300 and 300 > self.squares[0].ycor() > -300 and self.not_touching_itself()

    def not_touching_itself(self):
        for square in self.squares[1:]:
            if self.squares[0].distance(square) < 15:
                return False
        return True

    def increase_size(self):
        x = self.squares[len(self.squares) - 1].xcor()
        y = self.squares[len(self.squares) - 1].ycor()
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.pu()
        new_turtle.goto(x, y)
        self.squares.append(new_turtle)


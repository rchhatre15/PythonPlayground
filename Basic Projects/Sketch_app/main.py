from turtle import Turtle, Screen

t = Turtle()
s = Screen()

s.listen()


def clear_screen():
    t.clear()
    t.pu()
    t.home()
    t.pd()


def move_backward():
    t.forward(-10)


def move_forward():
    t.forward(10)


def move_clockwise():
    t.right(10)


def move_counterclockwise():
    t.left(10)


s.onkey(move_forward, "w")
s.onkey(move_backward, "s")
s.onkey(move_clockwise, "d")
s.onkey(move_counterclockwise, "a")
s.onkey(clear_screen, "c")


s.exitonclick()

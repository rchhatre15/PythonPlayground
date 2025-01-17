from turtle import Screen, Turtle
from scoreboard import Scoreboard
from obstacle import Obstacle
import random
import time

screen = Screen()
screen.setup(800, 600)
screen.title("Turtle Crossing")
screen.tracer(False)

scoreboard = Scoreboard()

t = Turtle("turtle")
t.pu()
t.setheading(90)
t.color("black")
t.goto(0, -280)


def move():
    t.forward(10)


screen.listen()
screen.onkey(move, "Up")
screen.onkey(move, "w")

obstacles = []
seconds = .1
count = 0

game_on = True
while game_on:
    screen.update()
    time.sleep(seconds)

    if t.ycor() > 280:
        t.goto(0, -280)
        scoreboard.increase_level()
        seconds -= seconds / 10

    count += 1
    if count == 10:
        obstacles.append(Obstacle())
        count = 0

    for o in obstacles:
        if -20 < o.xcor() < 20 and o.distance(t) < 25:
            game_on = False
            scoreboard.game_over()
            break
        o.refresh()


screen.exitonclick()

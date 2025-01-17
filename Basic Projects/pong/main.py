import turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from turtle import Screen
import time

screen = Screen()
screen.setup(800, 600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(False)

right_paddle = Paddle()
right_paddle.setpos(350, 0)

left_paddle = Paddle()
left_paddle.setpos(-350, 0)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_on = True
while game_on:
    screen.update()
    ball.refresh()
    time.sleep(.05)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce("y")
    elif ball.xcor() > 380 or ball.xcor() < -380:
        game_on = False
        scoreboard.game_over()
    elif ball.xcor() < -330 and ball.distance(left_paddle) < 50:
        ball.bounce("x")
        scoreboard.increase_left()
    elif ball.xcor() > 330 and ball.distance(right_paddle) < 50:
        ball.bounce("x")
        scoreboard.increase_right()





turtle.exitonclick()

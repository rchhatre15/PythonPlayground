from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

s = Screen()

s.setup(650, 650)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

s.listen()
s.onkey(snake.move_up, "Up")
s.onkey(snake.move_down, "Down")
s.onkey(snake.move_left, "Left")
s.onkey(snake.move_right, "Right")

game_on = True
while game_on:
    if not snake.game_on():
        scoreboard.reset()
        snake.reset()
    time.sleep(.075)
    snake.move()
    s.update()

    if snake.squares[0].distance(food) < 20:
        snake.increase_size()
        scoreboard.increase()
        food.refresh()


# over = Turtle()
# over.pu()
# over.color("white")
# over.speed("fastest")
# over.hideturtle()
# over.write("Game Over.", align="center", font=("Courier", 20, "normal"))


s.exitonclick()

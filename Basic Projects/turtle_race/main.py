from turtle import Turtle, Screen
import random

s = Screen()
s.setup(500, 500)

red = Turtle("turtle")
red.color("red")
red.pu()
red.goto(-230, -200)

green = Turtle("turtle")
green.color("green")
green.pu()
green.goto(-230, -125)

blue = Turtle("turtle")
blue.color("blue")
blue.pu()
blue.goto(-230, -50)

orange = Turtle("turtle")
orange.color("orange")
orange.pu()
orange.goto(-230, 50)


purple = Turtle("turtle")
purple.color("purple")
purple.pu()
purple.goto(-230, 125)

black = Turtle("turtle")
black.color("black")
black.pu()
black.goto(-230, 200)

user_bet = s.textinput("Make your bet", "Which color turtle will dub? ")

race = True
winner = ""
while race:
    red.forward(random.randint(0, 40))
    if red.xcor() >= 230:
        race = False
        winner = "red"
    else:
        green.forward(random.randint(0, 40))
        if green.xcor() >= 230:
            race = False
            winner = "green"
        else:
            blue.forward(random.randint(0, 40))
            if blue.xcor() >= 230:
                race = False
                winner = "blue"
            else:
                orange.forward(random.randint(0, 40))
                if orange.xcor() >= 230:
                    race = False
                    winner = "orange"
                else:
                    purple.forward(random.randint(0, 40))
                    if purple.xcor() >= 230:
                        race = False
                        winner = "purple"
                    else:
                        black.forward(random.randint(0, 40))
                        if black.xcor() >= 230:
                            race = False
                            winner = "black"

if user_bet == winner:
    print(f"You won! The winner was {winner}.")
else:
    print(f"You lost! The winner was {winner}.")

s.exitonclick()

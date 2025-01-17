import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

drawer = turtle.Turtle()
drawer.hideturtle()
drawer.color("Black")
drawer.pu()

data = pandas.read_csv("50_states.csv")

count = 0
guessed = []
while count != 50:
    guess = screen.textinput(title="Guess The States", prompt="Guess a State")
    if guess == "exit":
        break
    if guess in data["state"].to_list() and guess not in guessed:
        count += 1
        drawer.goto(int(data[data.state == guess]["x"]), int(data[data.state == guess]["y"]))
        drawer.write(guess)
        guessed.append(guess)

to_learn = []
for state in data["state"].to_list():
    if state not in guessed:
        to_learn.append(state)
pandas.DataFrame({"Focus up": to_learn}).to_csv("to_learn.csv")


turtle.mainloop()

from flask import Flask
import random as rand

app = Flask(__name__)

val = rand.randint(0,9)

def img_decorater(func):
    def wrapper(*args, **kwargs):
        func(args[0])
        if args[0] == 'correct':
            return func(args[0]) + '\n<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="correct">'
        elif args[0] == 'high':
            return func(args[0]) + '\n<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="high">'
        else:
            return func(args[0]) + '\n<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="low">'
    return wrapper

@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9!!</h1>" \
    "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"

@img_decorater
def high_page(status):
    return "<h1 style='color:red;'>Too high, try again!</h1>"

@img_decorater
def low_page(status):
    return "<h1 style='color:purple;'>Too low, try again!</h1>"

@img_decorater
def correct_page(status):
    return "<h1 style='color:green;'>You got it!</h1>"

@app.route("/<int:guess>")
def guess_page(guess):
    if guess > val:
        return high_page('high')
    elif guess < val:
        return low_page('low')
    else:
        return correct_page('correct')



if __name__ == "__main__":
    app.run()

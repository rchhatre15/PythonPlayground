import random
print("I'm thinkin of a number between 1 and 100.")
difficulty = input("Would you like to play on easy or hard?")
answer = random.randint(1, 100)
if difficulty == "easy":
    guess = 0
    while(not guess == answer):
        guess = int(input("Make a guess: "))
        if guess > answer:
            print("Too high")
        elif guess < answer:
            print("Too low")
        else:
            print("You got it")
else:
    count = 5
    guess = 0
    while(not guess == answer):
        guess = int(input("Make a guess: "))
        if guess > answer:
            print("Too high")
            count -= 1
            print(f"You have {count} guesses remaining")
        elif guess < answer:
            print("Too low")
            count -= 1
            print(f"You have {count} guesses remaining")
        else:
            print("You got it")

import random
print("Welcome to hangman. You have 6 guesses. Try not to fold!")

art = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = "rhythm wealth creative trustworthy".split()
word = words[random.randint(0, len(words) - 1)]
lives = 0
answer = []
for i in range(len(word)):
    answer.append('_')

while lives < 6 and answer.__contains__('_'):
    guess = input("Guess a letter: ")
    if(word.__contains__(guess)):
        for i in range(len(word)):
            if word[i] == guess:
                answer[i] = guess
        print("".join(answer))
        print(art[lives])
    else:
        lives += 1
        print("".join(answer))
        print(art[lives])
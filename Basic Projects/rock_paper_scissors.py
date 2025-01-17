import random
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
obstacle = random.randint(0,2)

if(choice == 0):
    print('''
        _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif(choice == 1):
    print('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')
else:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
print("Computer Choose")
if(obstacle == 0):
    print('''
        _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif(obstacle == 1):
    print('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')
else:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
if(choice == obstacle):
    print("You drew")
elif(choice == 0 and obstacle == 1 or choice == 1 and obstacle == 2 or choice == 2 and obstacle == 0):
    print("You lost")
else:
    print("You won")



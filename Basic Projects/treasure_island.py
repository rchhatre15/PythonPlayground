print('''         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
direction = input("You're at a crossroad. Where do you want to go? Type \"left\" or \"right\".\n")
if(direction == "left"):
    swim = input("You wanna swim accross lake or wait for a boat? Type \"swim\" or \"wait\".\n")
    if(swim == "wait"):
        door = input("Which door would you like to enter? Type \"red\" or \"blue\" or \"yellow\".\n")
        if(door == "red"):
            print("You sold and got burned by fire. Game Over.")
        elif(door == "blue"):
            print("You sold and got eaten by beasts. Game Over.")
        elif(door == "yellow"):
            print("Good shit. You found the treasure.")
        else:
            print("Invalid Input. Game Over.")
    else:
        print("You sold and got eaten by an alligator. Game over.")
else:
    print("You sold and fell into a hole. Game over.")

import math

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

drink = "on"
while not drink == "off":
    drink = input("What would you like? (espresso//latte//cappuccino): ")
    if drink == "report":
        print(f"water: {resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"money: ${resources['money']}")
    elif drink == "espresso":
        if resources['water'] < MENU['espresso']['ingredients']['water']:
            print("Sorry there is not enough water.")
        elif resources['coffee'] < MENU['espresso']['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
        else:
            total = .25 * int(input("Enter number of quarters: "))
            total += .1 * int(input("Enter number of dimes: "))
            total += .05 * int(input("Enter number of nickels: "))
            total += .01 * int(input("Enter number of pennies: "))
            if total < MENU['espresso']['cost']:
                print("Insufficient. Money refunded.")
            else:
                resources["water"] -= MENU['espresso']['ingredients']['water']
                # resources["milk"] -= MENU['espresso']['ingredients']['water']
                resources["coffee"] -= MENU['espresso']['ingredients']['coffee']
                resources["money"] += MENU['espresso']['cost']
                print(f"Here is ${math.ceil((total - MENU['espresso']['cost']) * 100) / 100} in change.")
                print("Enjoy your espresso!")
    elif drink == "cappuccino":
        if resources['water'] < MENU['cappuccino']['ingredients']['water']:
            print("Sorry there is not enough water.")
        elif resources['coffee'] < MENU['cappuccino']['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
        elif resources['milk'] < MENU['cappuccino']['ingredients']['milk']:
            print("Sorry there is not enough milk.")
        else:
            total = .25 * int(input("Enter number of quarters: "))
            total += .1 * int(input("Enter number of dimes: "))
            total += .05 * int(input("Enter number of nickels: "))
            total += .01 * int(input("Enter number of pennies: "))
            if total < MENU['cappuccino']['cost']:
                print("Insufficient. Money refunded.")
            else:
                resources["water"] -= MENU['cappuccino']['ingredients']['water']
                resources["milk"] -= MENU['cappuccino']['ingredients']['milk']
                resources["coffee"] -= MENU['cappuccino']['ingredients']['coffee']
                resources["money"] += MENU['cappuccino']['cost']
                print(f"Here is ${math.ceil((total - MENU['cappuccino']['cost']) * 100) / 100} in change.")
                print("Enjoy your cappuccino!")
    elif drink == "latte":
        if resources['water'] < MENU['latte']['ingredients']['water']:
            print("Sorry there is not enough water.")
        elif resources['coffee'] < MENU['latte']['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
        elif resources['milk'] < MENU['latte']['ingredients']['milk']:
            print("Sorry there is not enough milk.")
        else:
            total = .25 * int(input("Enter number of quarters: "))
            total += .1 * int(input("Enter number of dimes: "))
            total += .05 * int(input("Enter number of nickels: "))
            total += .01 * int(input("Enter number of pennies: "))
            if total < MENU['latte']['cost']:
                print("Insufficient. Money refunded.")
            else:
                resources["water"] -= MENU['latte']['ingredients']['water']
                resources["milk"] -= MENU['latte']['ingredients']['milk']
                resources["coffee"] -= MENU['latte']['ingredients']['coffee']
                resources["money"] += MENU['latte']['cost']
                print(f"Here is ${math.ceil((total - MENU['latte']['cost']) * 100) / 100} in change.")
                print("Enjoy your latte!")




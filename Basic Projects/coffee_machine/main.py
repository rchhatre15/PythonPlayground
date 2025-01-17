from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
mm = MoneyMachine()
menu = Menu()
drink = "on"
while not drink == "off":
    drink = input("What would you like? (espresso//latte//cappuccino): ")
    if drink == "report":
        cm.report()
        mm.report()
    else:
        item = menu.find_drink(drink)
        if item is not None:
            if cm.is_resource_sufficient(item):
                if mm.make_payment(item.cost):
                    cm.make_coffee(item)


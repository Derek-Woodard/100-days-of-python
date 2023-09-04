from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
menu = Menu()
mm = MoneyMachine()

ordering = True

while ordering:
    choice = input("What would you like? (espresso/latte/cappucinno)")

    if choice == 'report':
        cm.report()
        continue

    if choice == 'off':
        break

    drink = menu.find_drink(choice)
    
    
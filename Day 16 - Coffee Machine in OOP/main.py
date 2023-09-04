'''A program that imitates a coffee machine using Object Oriented Programming (OOP)'''
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
        mm.report()
        continue

    if choice == 'off':
        break

    drink = menu.find_drink(choice)

    if drink is None:
        continue

    if cm.is_resource_sufficient(drink):
        if mm.make_payment(drink.cost):
            cm.make_coffee(drink)

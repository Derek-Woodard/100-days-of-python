'''
A program that replicates the functionality of a coffee machine - customers purchase coffee
They pay for their drinks, then the resources in the coffee machine get depleted
'''

def check_resources(drink):
    '''Check if there are enough resources available to make the drink - return a list of all ingrediants that are short.'''
    short = []

    if resources["water"] < MENU[drink]["ingrediants"]["water"]:
        short.append("water")
    if resources["milk"] < MENU[drink]["ingrediants"]["milk"]:
        short.append("milk")
    if resources["coffee"] < MENU[drink]["ingrediants"]["coffee"]:
        short.append("coffee")

    return short

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
}

# Start by asking what the user would like, espresso/latte/cappuccino
# tell user to insert coins
# ask for quarters, then dimes, then nickels, then pennies.
# if the coins add up to more than the cost of the drink, tell the user what they get back in change
# Then give them their coffee using an emoji as well.
# if the coins don't add up to the cost, refund the user then ask what they would like again.
# track resources in the machine - each drinks takes a certain amount
# if a drink requires more of a resource than is available, say there is not enough.
# to do more, add funtcionality to refill the resources?

machine_on = True

money = 0.0

while machine_on:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")

    # Turn off the coffee machine (ie stop the program)
    if coffee_choice == 'off':
        exit()

    # Print a report on how many ingerdients there are
    elif coffee_choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['water']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")

    # Check to see if there are enough ingredients for the selected drink
    shorted = check_resources(coffee_choice)

    # If there are not enough resources available, tell the user, then loop back to the begining.
    if len(shorted) > 0:
        print(f"Sorry, there is not enough: {shorted}")
        continue    

    
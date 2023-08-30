from calculator_art import logo
import os

print(logo)

# continue condition
repeat = True

# condition for using a previous calculation
using_old_num = False

# Loop as long as the user wants to
while repeat:

    if not using_old_num:
        # Take the first number as input
        num_1 = float(input('What is the first number?: '))        

    # Determine which operation to use
    print('+\n-\n*\n/')
    operation = input('Pick an operation: ')

    # Take the second number as input
    num_2 = float(input('What is the next number?: '))

    if operation == '+':
        soln = num_1 + num_2
    elif operation == '-':
        soln = num_1 - num_2
    elif operation == '*':
        soln = num_1 * num_2
    elif operation == '/':
        soln = num_1 / num_2

    print(f'{num_1} {operation} {num_2} = {soln}')

    user_choice = input(f"Type 'y' to continue calculating with {soln}, type 'n' to start a new calculation, or type anything else to exit: ")

    if user_choice == 'y':
        using_old_num = True
        num_1 = soln
    elif user_choice == 'n':
        using_old_num = False
        os.system('cls')
        print(logo)
    else:
        exit()
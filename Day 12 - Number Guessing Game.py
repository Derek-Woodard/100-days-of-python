# Name spaces
# Local Scope - A variable created in a function only exists inside that finction. It is not accessible outside
# Global Scope - A variable created outside all functions can be accessed anywhere - even within functions
# to modify a global variable - in a function, you need to specifiy 'global variable_name' - not recommended
# better way to modify global with a function, you have access to the variable in the function, so use access, and return the modification as output
# Block Scope - Python does not have this - if you create a variable inside an if statement or loop, it is NOT exclusive to that statement or loop

import random
from number_guessing_art import logo
import os

keep_playing = True

while keep_playing:
    os.system('cls')
    print(logo)

    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    # Pick a random number from 1 to 100
    number = random.choice(range(1,100))

    # For testing purposes, reveal the number.
    print(f"Pssst, the correct answer is {number}")

    # Allow the player to choose their difficulty
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    # if easy chosen, 10 guesses, given too high or too low
    # if hard chosen, 5 guesses
    if difficulty == 'easy':
        guesses = 10
    else:
        guesses = 5

    # begin the guessing loop
    while guesses > 0:
        print(f"You have {guesses} attempts remaining to guess the number.")
        attempt = input("Make a guess: ")

        # If the guess is the correct number the player wins
        if attempt == number:
            print(f"You got it! The answer was {number}.")
            more = input("Do you want to play again? Type 'y' or 'n': ")

            if more == 'n':
                keep_playing = False
        
        # if the guess is higher than the number, tell the player
        elif attempt > number:
            print("Too High.\nGuess again.")
        
        # If the guess is lower than the number, tell the player
        else:
            print("Too Low.\nGuess again")

        guesses -= 1
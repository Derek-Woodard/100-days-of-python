import os
import random
from higher_lower_data import data
from higher_lower_art import logo, vs



def select_people():
    '''Select two people from the data list at random'''
    num_1 = random.choice(range(0,len(data)))
    num_2 = random.choice(range(0,len(data)))
    while num_2 == num_1: 
        num_2 = random.choice(range(0,len(data)))

    return data[num_1], data[num_2]

def compare(p_1, p_2):
    '''Compare two dictionaries to determine which has more followers. Return the person with more.'''
    if int(p_1['follower_count']) > int(p_2['follower_count']):
        return p_1
    else:
        return p_2

def display_choices(p_1, p_2):
    '''Display the choices for the player'''
    print(f"Compare A: {person_1['name']}, a {person_1['description']}, from {person_1['country']}.")
    print(vs)
    print(f"Against B: {person_2['name']}, a {person_2['description']}, from {person_2['country']}")

def player_guess(guess, p_1, p_2):
    '''check if player guess is correct'''
    if guess == 'a':
        choice = p_1
    else:
        choice = p_2

    higher = compare(person_1, person_2)

    if choice == higher:
        return True
    else:
        return False

keep_playing = True
# Outer loop for reseting the game
while keep_playing:
    score = 0

    playing = True
    while playing:
        # Clear the screen for the next round
        os.system('cls')

        print(logo)

        # If the player answers correctly, print that they were right and display their score.
        if score != 0:
            print(f"You're right! Current score: {score}")

        person_1, person_2 = select_people()
        display_choices(person_1, person_2)

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        if player_guess(guess, person_1, person_2):
            score += 1
        else:
            playing = False

    os.system('cls')
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")

    play_again = input("Play again: Type 'y' or 'n': ").lower()
    if play_again == 'n':
        keep_playing = False

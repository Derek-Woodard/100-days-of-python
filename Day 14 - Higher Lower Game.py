from higher_lower_data import data
from higher_lower_art import logo, vs
import random
import os


def select_people():
    '''Select two people from the data list at random'''
    num_1 = random.choice(range(1,51))
    num_2 = random.choice(range(1,51))
    while num_2 == num_1: 
        num_2 = random.choice(range(0,50))

    return data[num_1], data[num_2]

def compare(p_1, p_2):
    '''Compare two dictionaries to determine which has more followers. Return the person with more.'''
    if p_1['follower_count'] > p_2['follower_count']:
        return p_1
    else:
        return p_2

#playing = True
#while playing:
os.system('cls')
print(logo)

# pick two random selections from the data list.
# display their information. ex:
# Compare A: Taylor Swift, a Musician, from United States.
# print the vs art
# then print the second choice
# remove the two selected choices from the list?
# Ask "Who has more followers? Type 'A' of 'B': "
# player inputs - compare the follower amount of the selections
# if correct, add 1 to score, then clear screen, show the score and display a  new comparison
# if incorrect, display a final score and ask if they want to play again.

person_1, person_2 = select_people()
print(f"Compare A: {person_1['name']}, a {person_1['description']}, from {person_1['country']}.")
print(vs)
print(f"Against B: {person_2['name']}, a {person_2['description']}, from {person_2['country']}")
guess = input("Who has more followers? Type 'A' or 'B': ").lower()

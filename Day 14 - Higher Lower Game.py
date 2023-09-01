from higher_lower_data import data
from higher_lower_art import logo, vs
import random
import os


def select_people():
    # Select two people from the data list at random
    num_1 = random.choice(range(1,51))
    num_2 = random.choice(range(1,51))
    while num_2 == num_1: 
        num_2 = random.choice(range(0,50))

    return data[num_1], data[num_2]
#playing = True

#while playing:
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



print(person_1)
print(person_2)
import random

print("""\
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  
""")


# Set up a list of words that can be used as solutions
word_list = ["ardvark"]#, "baboon", "camel"]

# Set up number of lives that user has to lose
lives = 5

# Pick random word for the user to guess from the word list
chosen_word = random.choice(word_list)

# Generate a number of blanks equal to the number of letters in the random word
blanks = len(chosen_word)

# Take user input of one letter - force lower case
guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
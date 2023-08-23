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

# Set up game over condition for loop
game_over = False

# Set up a list of words that can be used as solutions
word_list = ["ardvark", "baboon", "camel"]

# Set up number of lives that user has to lose
lives = 6

# Pick random word for the user to guess from the word list
chosen_word = random.choice(word_list)

# Generate a number of blanks equal to the number of letters in the random word
blanks = []
for i in chosen_word:
    blanks.append("_")


tester = 0
# Start game loop
while tester < 5: #not game_over:
    # print the current ASCI art of the hangman


    # Print the current blanks and guessed letters
    print(blanks)

    # Take user input of one letter - force lower case
    guess = input("Guess a letter: ").lower()

    # Compare the user guessed letter to the random word
    index = 0
    for letter in chosen_word:
        if letter == guess:
            blanks[index] = guess
        index += 1
    tester += 1
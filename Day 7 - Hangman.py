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

hangman = ["""\
  +---+
  |   |
      |
      |
      |
      |
=========""",
"""\
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
"""\
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
"""\
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
"""\
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
"""\
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
"""\
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",]

# Set up a list of words that can be used as solutions
word_list = ["ardvark", "baboon", "camel"]

# Set up number of lives that user has to lose
lives_lost = 0

# Pick random word for the user to guess from the word list
chosen_word = random.choice(word_list)

# Generate a number of blanks equal to the number of letters in the random word
blanks = []
for i in chosen_word:
    blanks.append("_")

# Start game loop
while lives_lost < 6:
    # Take user input of one letter - force lower case
    guess = input("Guess a letter: ").lower()

    # Compare the user guessed letter to the random word
    guess_in_word = False
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            blanks[position] = guess
            guess_in_word = True
    
    if not guess_in_word:
        print(f"You guessed {guess}. That is not in the word. You lose a life.")
        lives_lost += 1

    # Print the current blanks and guessed letters
    print(blanks)
    
    # print the current ASCI art of the hangman
    print(hangman[lives_lost])

    if "_" not in blanks:
        print(f"You Win! Your word was {chosen_word}")
        exit()
    
    if lives_lost == 6:
        print("Game Over.")
        exit()
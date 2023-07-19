import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
while True: #if player choice is not rock paper or scissors, re-ask
    player = input('Rock, Paper, or Scissors? ').lower() # take input from user - make sure it's lower case
    computer_chioce = random.randint(1,3) #computer will random pick a number from 1-3 to reprsent their choice

    # display the player's choice
    if player == 'rock':
        print(f'You picked\n{rock}')
    elif player == 'paper':
        print(f'You picked\n{paper}')
    elif player == 'scissors':
        print(f'You picked\n{scissors}')
    else:
        print('Invalid selection')
        continue # reset the loop if choice is not valid

    # connect computer's random integer choice to a selection, then display their choice
    if computer_chioce == 1:
        print(f'You opponent picked\n{rock}')
    elif computer_chioce == 2:
        print(f'You opponent picked\n{paper}')
    else:
        print(f'You opponent picked\n{scissors}')

    # Select winner based on: rock beats scissors, paper beats rock, scissors beat paper - end while loop after selection is made
    if (player == 'rock' and computer_chioce == 3) or (player == 'paper' and computer_chioce == 1) or (player == 'scissors' and computer_chioce == 2):
        print('You Win!')
        break
    elif(player == 'rock' and computer_chioce == 2) or (player == 'paper' and computer_chioce == 3) or (player == 'scissors' and computer_chioce == 1):
        print('You Lose!')
        break
    else:
        print('Draw!')
        break

# features to add
# Ace can be either 1 or 11 - initially ace counts as 11, unless it pushes the player score over 21
# may need to use dictionaries after all as the deck of cards
# if dealer ends up with a score under 17, they need to take a card
# dealer should score based on player score as they shouldn't be able to see it

from blackjack_art import logo
import random
import os

# A list representing the values of a deck of cards
cards = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]

# a function that deals the initial cards to the player and the computer
def deal(p_cards, d_cards):
    for i in range(4):
        card = random.choice(cards)
        # As cards are added to the hands, they are removed from the deck
        cards.remove(card)
        if i < 2:
            player_cards.append(card)
        else:
            dealer_cards.append(card)

# A function that removes one card from the deck and adds it to the hand of the hand used as input
def hit_me(hand):
    card = random.choice(cards)
    cards.remove(card)
    hand.append(card)

# A function that determines the score of the hand used as input
def find_score(cards):
    score = 0
    for card in cards:
        score += card
    return score

# A condition for playing the game
playing = True

# The game loop
while playing:
    # Clear the screen and re-print the logo at the start of each game.
    os.system('cls')
    print(logo)
    
    # Initiate the two hands and deal the first two cards to each
    player_cards = []
    dealer_cards = []
    deal(player_cards, dealer_cards)

    # Initiate a continue condition for the player wanting more cards
    more_cards = True

    # Determine the initial score of the players
    player_score = find_score(player_cards)
    dealer_score = find_score(dealer_cards)

    # inner loop starts
    while player_score < 22 and more_cards:

        # Display the player's cards and score
        print(f'Your cards: {player_cards}, current score: {player_score}')
        
        # Computer/dealer only takes cards if their score is lower than 17
        if(dealer_score < 17):
            hit_me(dealer_cards)
            dealer_score = find_score(dealer_cards)
            
        # inform the player of the computer's first card (or if they don't take one)
        if len(dealer_cards) > 2:
            print(f"Computer's first card: {dealer_cards[2]}")
        else:
            print('Computer takes no cards')

        # Determine if the player wants another card
        keep_playing = input("Type 'y' to get another card, type 'n' to pass: ")

        # if the player wants another card, deal them a new card then continue the loop
        if keep_playing == 'y':
            hit_me(player_cards)
            more_cards = True

        # If the player doesn't want any more cards, end the loop and allow the computer to get their score higher than 17
        else:
            more_cards = False
            while dealer_score < 17:
                hit_me(dealer_cards)
                dealer_score = find_score(dealer_cards)

        # Update the scores
        player_score = find_score(player_cards)
        dealer_score = find_score(dealer_cards)

    # When the player decides to stop receiving new cards, show the final hands and scores
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")

    # Determine if the player won or lost.
    if player_score > 21:
        print("You went over. You lose.")
    elif player_score < dealer_score and dealer_score <= 21:
        print("You lose.")
    elif player_score == dealer_score:
        print("It's a draw.")
    elif dealer_score > 21 or player_score > dealer_score:
        print("You win!")

    # Ask the player if they want to play again.
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == 'n':
        playing = False
    else:
        playing = True


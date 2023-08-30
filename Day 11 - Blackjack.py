from blackjack_art import logo
import random
import os

#cards = {
#    1:[1,4],
#    2:[2,4],
#    3:[3,4],
#    4:[4,4],
#    5:[5,4],
#    6:[6,4],
#    7:[7,4],
#    8:[8,4],
#    9:[9,4],
#    10:[10,4],
#    'J':[10,4],
#    'Q':[10,4],
#    'K':[10,4]
#}
cards = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]

def deal(p_cards, d_cards):
    for i in range(4):
        card = random.choice(cards)
        cards.remove(card)
        if i < 2:
            player_cards.append(card)
        else:
            dealer_cards.append(card)

def hit_me(hand):
    card = random.choice(cards)
    cards.remove(card)
    hand.append(card)

def find_score(cards):
    score = 0
    for card in cards:
        score += card
    return score

    
player_cards = []
dealer_cards = []

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play == 'n':
    playing = False
else:
    playing = True

first_turn = True

while playing:
    os.system('cls')
    print(logo)
    deal(player_cards, dealer_cards)

    more_cards = True
    player_score = 0

    # inner loop starts
    while player_score < 21 and more_cards:
        player_score = find_score(player_cards)
        dealer_score = find_score(dealer_cards)

        print(f'Your cards: {player_cards}, current score: {player_score}')
        
        if(dealer_score < 21 and dealer_score < player_score):
           hit_me(dealer_cards)
            
        if len(dealer_cards) > 2:
            print(f"Computer's first card: {dealer_cards[2]}")
        else:
            print('Computer takes no cards')

        keep_playing = input("Type 'y' to get another card, type 'n' to pass: ")
        if keep_playing == 'y':
            hit_me(player_cards)
            more_cards = True
        else:
            more_cards = False

        player_score = find_score(player_cards)
        dealer_score = find_score(dealer_cards)


    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")


        

    playing = False


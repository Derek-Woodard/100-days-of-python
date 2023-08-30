from blackjack_art import logo
import random

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

while playing:
    deal(player_cards, dealer_cards)
    print(player_cards)
    print(dealer_cards)

    player_score = find_score(player_cards)
    dealer_score = find_score(dealer_cards)

    print(f'Your cards: {player_cards}, current score: {player_score}')
    print(f'Your cards: {dealer_cards}, current score: {dealer_score}')
    playing = False


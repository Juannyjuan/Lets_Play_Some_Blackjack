# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 17:01:25 2023

This is a Blackjack strategy testing project

@author: Juan
"""

import random

# initialise a deck of cards first

ranking = []
for i in range (9):
    ranking.append(i+1)
for i in range(4):
    ranking.append(10)

deck = ranking*4
# print(len(deck)) # this should return 52
## we ignore the suits because we merely care about the numerical values in blackjack

## now ranking has one of each card, to make a full deck we multiply by 4

def shuffle_deck():
    deck = ranking*4
    return deck

def hit():
    random_card = random.choice(deck) # randomly draws one card without replacement
    return random_card

# gameplay

## player hits, dealer hits, player hits
## we ignore the 4th hit for dealer because its unknown

# initialise each other's hand

dealer_hand = 0
player_hand = 0

dealer_hand += hit()
player_hand += hit()*2

print(f"For the first dealt: dealer has {dealer_hand}")
print(f"For the first dealt: player has {player_hand}", "player executes its strategy", sep = "\n")


# here comes the automatic strategy
while player_hand < 15:
    player_hand += hit()

if player_hand > 21:
    print(f"Player has busted with {player_hand} in hand", "Dealer wins this game", sep = "\n")
else:
    while dealer_hand < player_hand:
        dealer_hand += hit()
    print(f"dealer has {dealer_hand}")
    print(f"player has {player_hand}")
    if dealer_hand > 21:
        print("Dealer goes bust, Player wins this game")
    elif dealer_hand >= player_hand:
        print("Dealer wins this game")
    else:
        print("Player wins this game")


shuffle_deck()

def player_turn(player):
    card  = deck.pop()
    print player + "drew" + str(card)
    return str(card)

import random
def shuffled_deck():
	deck = range(2, 52)
	random.shuffle(deck)
	return deck

deck=[]
hand= shuffled_deck()
deck.extend(hand)

player1= raw_input("What's your name:")
player2=raw_input("What's your name:")

player1_score=0
player2_score= 0


player_turn(player1)
player_turn(player2)

while deck:
    if player_turn(player1) > player_turn(player2):
    player1_score = player1_score +1
    print player1_score
elif player_turn(player2) > player_turn(player1):
    player2_score=player2_score+1
    print(player2_score)

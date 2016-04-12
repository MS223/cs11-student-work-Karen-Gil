import random
def shuffled_deck():
	basic_deck = range(2, 52)
	random.shuffle(basic_deck)
	return basic_deck

player1= raw_input("What's your name:")
player2=raw_input("What's your name:")

Player#start here
def player_turn (player):
    card= deck.pop()
    print player1 + "drew" + card
    return str(card)

player_turn(player1)
player_turn(player2)

if player1 > player2:
    player1_score +1
elif player2 > player1:
    player2_score +1

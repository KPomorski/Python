import random


def dealer_choice(d_cards, p_cards, deck):
	p_value = sum(p_cards)
	if p_value > 21:
		print("You busted, Dealer wins!")
		exit()
	d_value = sum(d_cards)
	while d_value < 17:
		d_cards.append(deck.pop())
		d_value = sum(d_cards)
	print("Dealer has " + str(d_value) + " with the cards ", d_cards)
	if d_value > 21:
		print("Dealer Busts, you win!")
		exit()
	elif d_value == 21:
		if p_value == 21:
			print("The match is tie!")
			exit()
		else:
			print("Dealer has Blackjack, and wins!")
			exit()
	elif p_value == 21:
		print("Player has blackjack, Player wins!")
		exit()
	elif p_value == d_value:
		print("Game is a tie!")
		exit()
	elif p_value < d_value:
		print("Dealer Wins!")
		exit()
	elif p_value > d_value:
		print("Player wins!")
		exit()


def check_hand(hand):
	if hand > 21:
		return 1
	elif hand > 21:
		return 0
	else:
		return 2
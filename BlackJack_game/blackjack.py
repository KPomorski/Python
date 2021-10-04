# BLACK JACK - CASINO

import random
from bjfunc import check_hand, dealer_choice

print("                       **********************************************************                                    ")
print("                                   Welcome to the game Casino - BLACK JACK !                                         ")
print("                       **********************************************************                                    ")

deck=[1,2,3,4,5,6,7,8,9,10,10,10,10,11]*4

#Initial shuffle of deck jn m
d_cards = []                     #Initialising dealer's cards
p_cards = []                     #Initialising player's cards
d_hand = 0
p_hand = 0

while len(d_cards) < 2:
	d_cards.append(deck.pop())
	d_hand = sum(d_cards)
	p_cards.append(deck.pop())
	p_hand = sum(p_cards)
	if len(d_cards) == 2:
		print('The dealer is showing ', d_cards[1])
		print("The Player has ", p_cards, " for a total of ", p_hand)

p_busted = check_hand(p_hand)
while p_busted != 1:
	k = input('Want to hit or stay?\n Type h for hit and s for stay ')
	if k == 'h':
		p_cards.append(deck.pop())
		print ('You have a total of ' + str(sum(p_cards)) + ' with the cards ', p_cards)
		p_busted = check_hand(sum(p_cards))
		if p_busted == 1:
			print('You BUSTED!\n Dealer Wins !!')
			exit()
	elif k == 's':
		dealer_choice(d_cards, p_cards, deck)
		break
	else:
		print('Please reply with a 0 or a 1.')
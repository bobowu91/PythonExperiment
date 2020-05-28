import pypoker as pp
import random

'''
myhands = pp.draw_cards(2)

flop = pp.draw_cards(3)
print(myhands, flop)
pp.assess_hands(myhands, flop)

turn = pp.draw_cards(1)
print(turn)
pp.assess_hands(myhands, flop+turn)

river = pp.draw_cards(1)
print(river)
pp.assess_hands(myhands, flop+turn+river)
'''

number_of_players = 6
players = [pp.draw_cards(2) for i in range(number_of_players)]
flop = pp.draw_cards(3)
turn = pp.draw_cards(1)
river = pp.draw_cards(1)

for p in players:
    print(p)
# I will be player 6
myhands = players[-1]
print(myhands)
print(flop)
pp.assess_hands(myhands, flop)
print(turn)
pp.assess_hands(myhands, flop+turn)
print(river)
pp.assess_hands(myhands, flop+turn+river)

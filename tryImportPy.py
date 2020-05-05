import pypoker


a = ['S8', "DT"]
b = ['S7', 'D5', 'CQ']
c = ['SA', 'H8', 'H9', 'D3']

# 1
pypoker.assess_hands(a)
# 2
pypoker.assess_hands(a, b)
# 3
pypoker.assess_hands(a, c, n_sim=200)


'''
**********************************************************************
only value checking needed:
1. Full House: check if one number appears 3 times and another 2 times
2. 4 of a kind: check if one number appears 4 times
3. Straight:
4. 3 of a kind: check if one number appears 3 times
5. two pairs: check if two numbers, each appears 2 times
6. one pair: check if one number appears 2 times

suit info also needed:
1. Flush
2. Straight flush
**********************************************************************
import random
random.seed(88)

# value dictionary can be replaced by pypoker.value
value = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
         '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10,
         'J': 11, 'Q': 12, 'K': 13, 'A': 14}

# draw cards for players
players = {}
for i in range(number_of_players):
    players[i+1] = list(draw_cards(2))

# draw cards for open tables
tables_keys = ['flop1', 'flop2', 'flop3', 'turn', 'river']
tables_values = draw_cards(5)
tables = dict(zip(tables_keys, tables_values))

result = check_hands(players[1], tables, 5)
print(players[1])
print(result)

print(a[0])
print(a[0][0], a[0][1])
print(a[1])
print(a[1][0], a[1][1])
print(value[a[0][1]] < value[a[1][1]])


if a[0][1] == a[1][1]:
    print("pair")
elif a[0][0] == a[1][0]:
    print("suit")
else:
    print("no pair and no suit")

# me = pypoker.draw_cards(2)
# bb = pypoker.draw_cards(2)
# tables = pypoker.draw_cards(5)
# print(me, bb, tables)
# print(pypoker.has_flush(me + tables), pypoker.has_straight(me + tables))
# print(pypoker.has_flush(bb + tables), pypoker.has_straight(bb + tables))

# myhands = me + tables
# print(myhands)

# myhands_value = [value[i[1]] for i in myhands]
# print(myhands_value)
#
# freq_dict = {}
# for i in set(myhands_value):
#     freq_dict[i] = myhands_value.count(i)
#
# freq_list = sorted(freq_dict.values())
# print(freq_dict)
# print(freq_list)
# print(sorted(freq_list)[-1], sorted(freq_list)[-2])
# print(max(freq_dict.values()), min(freq_dict.values()))

# print(f"Straight:{pypoker.has_straight(myhands)}")
# print(f"Flush:{pypoker.has_flush(myhands)}")
# print(pypoker.evaluation(myhands))

# eg1 = ['CQ', 'C10', 'D5', 'CJ', 'S10', 'CA', 'CK']
# eg = ['C6', 'C10', 'C3', 'C5', 'C7', 'D4', 'D3']
# print(pypoker.has_straight(eg1))
# print(pypoker.evaluation(eg1))

## scenario 1: probabilty distribution

hands = pypoker.poker_simulation(10000, 7)
result = []
for hand in hands:
    result.append(pypoker.evaluation(hand))

stats = {}
for item in set(result):
    stats[item] = result.count(item)/10000

print(stats)

## scenario 2:
my_hands = pypoker.draw_cards(2)
table_sim = pypoker.poker_simulation(10000, 5)
print(my_hands)
result = []
for i in range(len(table_sim)):
    combo = my_hands + table_sim[i]
    result.append(pypoker.evaluation(combo))

stats = {}
for item in set(result):
    stats[item] = result.count(item)/10000
print(stats)

n_simulation = 1000
n_sim_cards = 5

my_hands = pypoker.draw_cards(2)
hand_sim = pypoker.poker_simulation(n_simulation, n_sim_cards)
for i in range(len(hand_sim)):
    hand_sim[i] = my_hands + hand_sim[i]

print(my_hands)
pypoker.stats_distribution(hand_sim)
m = pypoker.poker_simulation(n_simulation, 5)
m_unique = [a+i for i in m if pypoker.check_unique(a+i)]
print(len(m_unique))
pypoker.stats_distribution(m_unique)
'''

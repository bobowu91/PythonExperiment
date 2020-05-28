import pypoker
import numpy as np

'''
a = ['HK', 'CQ']
b = ['HT', 'DT']
c = ['DA', 'D9']

# x = pypoker.assess_hands(a)
# print(x)
n_sim = [200]
flush_std = []
flush_avg = []
for sim in n_sim:
    tlist = []
    flush = []
    for i in range(100):
        tlist.append(pypoker.assess_hands(a, n_sim=sim))
        # flush = [item['flush'] for item in tlist]
        for item in tlist:
            if 'flush' in item:
                flush.append(item['flush'])
            else:
                flush.append(0)
    flush_std.append(np.std(flush))
    flush_avg.append(np.mean(flush))
print(f"{flush_avg[0]: .2%}")
print(flush_std)
'''
# pypoker.player_chance([a, b, c])

'''
e = ['D7', 'DA', 'D2', 'D3', 'H4', 'HA', 'DJ']  # flush hands
f = ['D7', 'C5', 'C4', 'H8', 'HA', 'S6', 'S9']  # straight
i = ['DQ', 'DJ', 'HT', 'H9', 'H3', 'D4', 'HK']  # straight
g = ['H5', 'HT', 'C7', 'C9', 'S6', 'CT', 'ST']  # 3 of a kind
h = ['S6', 'D5', 'S5', 'H7', 'C5', 'C7', 'HQ']  # full house
**********************************************************************
only value checking needed:
1. full House: check if one number appears 3 times and another 2 times
2. 4 of a kind: check if one number appears 4 times
3. Straight:
4. 3 of a kind: check if one number appears 3 times
5. two pairs: check if two numbers, each appears 2 times
6. one pair: check if one number appears 2 times

suit info also needed:
1. flush
2. straight flush
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

def momo(hands):

    myhands = [[item[0], item[1], value[item[1]]] for item in hands]
    f_l = [hand[1] for hand in myhands]
    for j in range(len(f_l)):
        myhands[j].append(f_l.count(f_l[j]))
    myhands.sort(key=lambda x: x[2])
    print(f_l)
    print([f_l.count(i) for i in set(f_l)])
    print(myhands)


def trylist(x, *y):
    print(x)
    print(y)
    for i in y:
        print(type(i))
        print(type(x))
        print(x + i)

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

# scenario 1: probabilty distribution

hands = pypoker.poker_simulation(10000, 7)
result = []
for hand in hands:
    result.append(pypoker.evaluation(hand))

stats = {}
for item in set(result):
    stats[item] = result.count(item)/10000

print(stats)

# scenario 2:
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

# 1
pypoker.assess_hands(a)
# 2
pypoker.assess_hands(a, b)
# 3
pypoker.assess_hands(a, c, n_sim=200)

# total = 6000
# table = pypoker.poker_simulation(total, 5)
# result = []
# chance = []
# lu = ['HK', 'CQ']
# mu = ['HT', 'DT']
# nu = ['DA', 'D9']
# for i in table:
#     a = ['HK', 'CQ']
#     b = ['HT', 'DT']
#     c = ['DA', 'D9']
#     if pypoker.check_unique(a+b+i):
#         x = pypoker.check_winner(i, [a, b, c])
#         result.append(x[0:2])
#
# for item in [lu, mu, nu]:
#     chance.append(result.count(item)/len(result))
# print(chance)

# for i in set(result):
#     prob = result.count(i)/len(result)
#     print(f"The hand {i} has chance of {prob: .2%}")


# print(f"a is {a}")
# print(f"The table is {table}")
# print(f"b is {b}")
# print(f"c is {c}")
# print(f"d is {d}")
# pypoker.assess_hands(a)

# for i in range(100):
#     print(i)
#     a = pypoker.poker_simulation(1, 2)[0]
#     table = pypoker.poker_simulation(1, 5)[0]
#     if pypoker.check_unique(a + table):
#         pypoker.check_winner(table, a)
#
'''

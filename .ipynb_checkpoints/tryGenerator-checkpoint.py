import pypoker as pp

table = pp.draw_cards(5)
a = pp.draw_cards(2)
b = pp.draw_cards(2)
c = pp.draw_cards(2)
d = pp.draw_cards(2)
a, b, c, d = [['H8', 'HA'], ['D3', 'ST'], ['S6', 'CQ'], ['CA', 'C4']]
print(a, b, c, d)
# x = pp.check_winner(table, [a, b, c, d])
# print(x)
print("********************************")
pp.player_chance_new([a, b, c, d], n_sim=200)

'''
Table is ['D3', 'D4', 'H8', 'C3', 'H4']
[['S8', 'D2'], ['D7', 'HT'], ['C6', 'C5'], ['ST', 'DA']] reach a tie.
[['S8', 'D2'], ['D7', 'HT'], ['C6', 'C5'], ['ST', 'DA']]


digit_gen = (value[i[1]] for i in hands)
print(digit_gen)
m = set()
for i in digit_gen:
    m.add(i)
print(m)

x = {1, 2, 3, 4}
x.add(5)
print(len(x))

for i in range(1, 4):
    print(-i)
hands = ['DQ', 'D9', 'H5', 'HA', 'H3', 'D4', 'HK']
print(pp.has_straight_new(hands))
'''
'''
value = {'2': 2, '3': 3, '4': 4, '5': 5,
         '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10,
         'J': 11, 'Q': 12, 'K': 13, 'A': 14}

result_value = {'straight flush': 1000,
                '4 of a kind': 900,
                'full house': 800,
                'flush': 700,
                'straight': 600,
                '3 of a kind': 500,
                'two pairs': 400,
                'one pair': 300,
                'all singles': 200}


if we know there are N possible outcomes for the event, how many runs
should we perform to accurately simulate the reality? I think it should be at
least more than the number of possible outcomes

####### generator examples ##########
def get_pop(population):
    for i in population:
        yield i

population = ['a', 'b', 'c', 'd']
item = get_pop(population)
print(item)
print(next(item))
print(next(item))
print(next(item))

# with poker_simulation yield instead of return
hands_gen = pp.poker_simulation(n_hands=5)
nl = next(hands_gen)
for i in range(5):
    print(nl[i])


# about 0.27 sec for 5000 runs; not much increase to 1 billion
# hands = pp.cards_simulation(n_simulation=100000000, n_hands=5)
# print(hands)
# for i in range(20):
#     print(next(hands))
#     print(i)
#
# similar time for 5000 runs; extremely long time for 1 billion
# hands = pp.poker_simulation(n_simulation=100000000, n_hands=5)
# for i in hands[0:21]:
#    print(i)


***************************************************************
simulate 80,000 hands with a certain hands for uniqueness
generator yield method is 0.2 sec faster than return methd
# mycards = ['DA', 'DT']
# hands = pp.cards_simulation(80000, 5)
# c = 0
# for hand in hands:
#     combo = mycards + hand
#     if not pp.check_unique(combo):
#         c = c+1
#         print(f"this hand {combo} is not unique")
# print(c)


# hands = pp.poker_simulation(80000, 5)
# c = 0
# for hand in hands:
#     combo = mycards + hand
#     if not pp.check_unique(combo):
#         c = c+1
#         print(f"this hand {combo} is not unique")
# print(c)
***************************************************************
n_simulation = 500000
f_hands = pp.cards_simulation(n_simulation=n_simulation, n_hands=7)
c = 0
for hand in f_hands:
    if pp.has_flush(hand):
        c = c + 1
print(f"{c/n_simulation: .2%}")

***************************************************************
cards = ['D6', 'D8']
table1 = ['DA', 'D5', 'S7']  # check flush and straight
table2 = ['DA', 'S5', 'S7']  # check straight
n_simulation = 200000
f_hands = pp.cards_simulation(n_simulation=n_simulation, n_hands=2)
c = 0
for hand in f_hands:
    combo = cards + table1 + hand
    if pp.check_unique(combo):
        if pp.has_flush(combo):
            c = c + 1
        if pp.has_straight(combo):
            c = c+1
print(f"{c/n_simulation: .2%}")
**********************************************************
simulation = 1
cards = 7

hands = pp.cards_simulation(n_simulation=simulation, n_hands=7)
prob = pp.stats_distribution(hands)
a = b = c = 0
a = a+2
print(a, b, c)

'''

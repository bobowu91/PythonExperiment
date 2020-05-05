'''
import pandas as pd
import numpy as np
x = 5
y = 6
print(x + 6)

tables_keys = ['first', 'second', 'third', 'flop', 'river']
values = [1, 2, 3]
tables = dict(zip(tables_keys, values))

print(tables)

tables['flop'] = 4
print(tables)


num = list(range(1, 14))
suit = ['Hearts', "Clubs", 'Diamonds', 'Spades']
print(num, suit)

np.random.seed(88)
df = pd.DataFrame(np.random.randint(0, 2, [4, 13]), index=suit, columns=num)

print(df)
print(df.loc["Hearts"].sum())


x = [1, 2, 3]
y = x.copy()
print(y.pop(2))
print(x, y)

dic = {'Apple': 13,
       "Banana": 4,
       "Pear": 5}

m_dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}
print(m_dic)


dic_l = {'hand1': ['c', 10],
         "hand2": ['s', 2],
         "flop1": ['s', 5],
         "flop2": ['d', 5],
         "flop3": ['s', 10],
         "turn": ['c', 5],
         "river": ['h', 10]}

new = {k: v for k, v in sorted(dic_l.items(), key=lambda item: item[1][1])}
print(new)

flush = {'hand1': ['s', 10],
         "hand2": ['s', 2],
         "flop1": ['d', 5],
         "flop2": ['s', 5],
         "flop3": ['s', 7],
         "turn": ['c', 5],
         "river": ['s', 9]}
new = {k: v for k, v in sorted(flush.items(), key=lambda item: item[1][0])}
print(new)


for i in mm:
    if i == 5:
        print('good')
else:
    print('bad')

'''

import pypoker
mm = [1, 2, 3, 4]
eg = ['C6', 'C2', 'C3', 'C9', 'C7', 'D4', 'D3']
pypoker.assess_hands(['a'], tables=eg, n_sim=1000)


def check(m):

    for i in m:
        print(f"this has been run for the {i}-th time")
        if i == 9:
            print('true is done')
            return True
    else:
        print('false is done')
        return False

    print("Do we make it here?")
    return 0


def find(m):

    if m == 1:
        return 1
    if m == 2:
        return m*2
    if m == 3:
        return m*3
    if m < 7:
        return 7*m


eg = ['C6', 'C2', 'C3', 'C9', 'C7', 'D4', 'D3']


def dodo(hands):
    return True, hands


tz = dodo('mm')
print(tz[1])


for i in eg:
    print(i[1])
    if i[1] < '4':
        eg.remove(i)
print(eg)

import random
import statistics
import copy

cards_values = list(range(2, 10))
cards_values.extend(['T', 'J', 'Q', 'K', 'A'])
suits = ['H', 'D', 'C', 'S']  # Hearts; Diamonds; Clubs; Spades
cards = [''.join([y, str(x)]) for x in cards_values for y in suits]
number_of_players = 3

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


def draw_cards(n):  # draw any number of random cards.
    hands = random.sample(cards, n)
    for i in hands:
        cards.remove(i)
    return hands


def cards_simulation(n_simulation=5000, n_hands=3):
    '''
    draw N number of cards with no replacement;
    if concatenate with other hands, it might generate duplicate, use with
    check_unique() function to remove the entire duplicate entry.

    input: number of simulation runs and how many cards to be drawed
    output: a generator object containing hands of number N
    '''
    for i in range(n_simulation):
        yield random.sample(cards, n_hands)


def check_unique(hands):
    if len(set(hands)) == len(hands):
        return True
    else:
        return False


def has_flush(hands):
    '''
    check if there is a pattern of flush in the hands;
    input type is a list of strings of any quantity
    '''

    table_suit = [i[0] for i in hands]
    for item in set(table_suit):
        if table_suit.count(item) >= 5:
            return item
    else:
        return False


def has_straight(hands):
    '''
    check if there is a pattern of straight in the hands;
    input type is a list of strings of any quantity
    '''
    m = set()  # Set will sort the list of interger from low to high
    digit = (value[i[1]] for i in hands)
    for i in digit:
        m.add(i)
    digit = list(m)
    length = len(digit) - 3

    if {2, 3, 4, 5, 14}.issubset(digit):
        return 5
    for i in range(1, length):
        if (digit[-i] - 4) == digit[-(i+4)]:
            return digit[-i]
    else:
        return False


def evaluation(hands):
    '''
    input should be a list of at least 5 cards
    return which best hand it is
    '''
    myhands_value = [value[i[1]] for i in hands]
    freq_dict = {}
    for i in set(myhands_value):
        freq_dict[i] = myhands_value.count(i)

    temp = [k for k, v in sorted(freq_dict.items(), key=lambda x: x[1])]
    freq_list = sorted(freq_dict.values())
    # [print(k, v) for k, v in sorted(freq_dict.items(), key=lambda x:x[1])]
    # print(temp)
    # print(freq_list)

    flush_info = has_flush(hands)

    if flush_info:
        besthands = [i for i in hands if i[0] == flush_info]
        tf = [value[item[1]] for item in besthands]
        # to extract the highest card
        if has_straight(besthands):
            return ('straight flush', max(tf))
        else:
            return ('flush', max(tf))
    elif max(freq_list) == 4:
        return ('4 of a kind', temp[-1])
    elif (max(freq_list) == 3) & (freq_list[-2] >= 2):
        return ('full house', temp[-1], temp[-2])
    elif has_straight(hands):
        return ('straight', has_straight(hands))
    elif (max(freq_list) == 3) & (freq_list[-2] < 2):
        return ('3 of a kind', temp[-1], temp[-2])
    elif max(freq_list) == 2:
        if freq_list[-2] == 2:
            return ('two pairs', temp[-1], temp[-2], temp[-3])
        else:
            return ('one pair', temp[-1], temp[-2])
    else:
        return ('all singles', temp[-1], temp[-2])


def stats_distribution(hands):
    '''
    Input is a nested list consist of hands of 5 cards to 7 cards
    evaluation of your hands against the table 5 cards
    this function assumes each hand has no repeated cards
    '''
    result = []
    for hand in hands:
        result.append(evaluation(hand)[0])
    stats = {}
    for item in set(result):
        stats[item] = result.count(item)/(len(result))
    [print(f"{k:16}", f"{value:.2%}")
     for k, value in sorted(stats.items(), key=lambda x: x[1])]
    # return stats


def assess_hands(hands, tables=[], n_sim=6000):
    '''
    pass your hands to see if you should continue to play
    input: hands is your hand_sim; table can range from 3 to 5 cards in a list
    '''
    combo = hands + tables
    if len(combo) == 7:
        print(evaluation(combo))
    else:
        handsim = poker_simulation(n_sim, 7-len(combo))
        ph = [combo + hand for hand in handsim if check_unique(combo + hand)]
        # print(len(ph)) # use this line to see how many simulations are run
    return stats_distribution(ph)


def check_winner(table, others):
    '''
    return the winner hand
    input all 5 table cards first; then take any number of hand
    others has to be a nested list of any number of hands

    '''
    temp = copy.deepcopy(others)
    for hand in temp:
        player_hands = evaluation(hand + table)
        player_value = result_value[player_hands[0]]

        if len(player_hands) == 2:
            bias = player_hands[1]
        elif len(player_hands) == 3:
            bias = player_hands[1] + 0.1 * player_hands[2]
        else:
            bias = (player_hands[1] + 0.1 * player_hands[2]
                    + 0.01 * player_hands[3])
        hand.extend([player_value + bias, player_hands[0]])

    # print(temp) # just in case we want to see the comparison for debug
#    for i in range(len(temp)):
#        if temp[i][2] > max:
#            max = temp[i][2]
#            counter = i
    # finding the global max
    max = tie = 0
    for index, item in enumerate(temp):
        if item[2] > max:
            max = item[2]
            counter = index
    # check if there is more than one max
    tie_hands = []
    for index, item in enumerate(temp):
        if item[2] == max:
            tie_hands.append(others[index])
            tie = tie + 1
    # if tie then return tie hands; otherwise return winner

    if len(tie_hands) == 1:
        # winner = temp[counter]
        # print(f"The winner is {winner[0], winner[1]} with {winner[3]}")
        return others[counter]
    else:
        # print(f"{tie_hands} reach a tie.")
        return tie_hands, 'tie'


def player_chance(player_hands, n_sim=8000):
    '''
    Input: players is a nested list of any players' hands
    '''
    # players = copy.deepcopy(player_hands)
    result, chance, con = [], [], []
    for i in player_hands:
        con = con + i
    table = cards_simulation(n_sim, 5)

    for card in table:
        # pp = copy.deepcopy(player_hands)
        if check_unique(con + card):
            x = check_winner(card, player_hands)
            if x[-1] == 'tie':
                result.append('tie')
            else:
                result.append(x)
    for item in player_hands:
        chance.append(result.count(item)/len(result))
    prob_tie = result.count('tie')/len(result)
    for i, num in enumerate(chance):
        print(f"The chance of player{i+1} winning is {num: .2%}.")
    print(f"The chance a tie game is {prob_tie:.2%}.")


def player_chance_new(player_hands, n_sim=8000):
    '''
    Input: players is a nested list of any players' hands
    '''
    # players = copy.deepcopy(player_hands)
    result, chance, con = [], [], []
    for i in player_hands:
        con = con + i
    table = cards_simulation(n_sim, 5)

    me = tie = counter = 0
    bobo = player_hands[0]
    bobos = set(bobo)
    cond = []

    for card in table:
        # pp = copy.deepcopy(player_hands)
        if check_unique(con + card):
            counter = counter + 1
            x = check_winner(card, player_hands)
            if x == bobo:
                me = me + 1

            if x[-1] == 'tie':
                for a in x[0]:
                    cond = cond + a
                if bobos.issubset(cond):
                    tie = tie + 1
    mewin = me/counter
    metie = tie/counter

    print(mewin, metie)


# Don't Use the Functions Below


def winner_hands(a, b, table):
    '''
    compare two hands and return the better one
    input: a and b are two hands; table is five table cards
    not meant for use of actual multiplayers
    '''
    a_hand = evaluation(a + table)[0]
    b_hand = evaluation(b + table)[0]

    a_val = result_value[a_hand]
    b_val = result_value[b_hand]

    if a_val == b_val:
        return f"Same Hands Type: {a_hand}"  # check the high cards
    elif a_val < b_val:
        return f"{b} hits {b_hand}"
    else:
        return f"{a} hits {a_hand}"


def has_straight_old(hands):
    '''
    check if there is a pattern of straight in the hands;
    input type is a list of strings of any quantity
    '''

    table_digit = [value[i[1]] for i in hands]
    table_digit = list(set(table_digit))
    # Set will sort the list of interger from low to high

    if {2, 3, 4, 5, 14}.issubset(table_digit):
        return 5
    for i in reversed(range(len(table_digit)-4)):
        if statistics.variance(table_digit[i:i+5]) == 2.5:
            return table_digit[i+4]  # istead of True, we can put a string
    else:
        return False


def poker_simulation(n_simulation=5000, n_hands=3):
    '''
    draw multiple hands of cards with possible replacement
    input: number of simulation runs and how many cards to be drawed
    output: a nested list of n cards
    '''
    hands_simulation = []
    for i in range(n_simulation):
        hands_simulation.append(random.sample(cards, n_hands))
    return hands_simulation  # could also work with yield hands_simulation

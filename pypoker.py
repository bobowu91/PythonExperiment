import random
import statistics

cards_values = list(range(2, 10))
cards_values.extend(['T', 'J', 'Q', 'K', 'A'])
suits = ['H', 'D', 'C', 'S']  # Hearts; Diamonds; Clubs; Spades
cards = [''.join([y, str(x)]) for x in cards_values for y in suits]
number_of_players = 3

value = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
         '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10,
         'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def poker_simulation(n_simulation=5000, n_hands=3):
    hands_simulation = []
    for i in range(n_simulation):
        hands_simulation.append(random.sample(cards, n_hands))
    return hands_simulation


def draw_cards(n):
    # draw any number of random cards.
    hands = random.sample(cards, n)
    for i in hands:
        cards.remove(i)
    return hands


# def check_hands(player_hands, table_cards, n):
#     table_cards = list(table_cards.values())[0:n]
#     total_combo = player_hands + table_cards
#     return total_combo

def check_unique(hands):
    if len(set(hands)) == len(hands):
        return True
    else:
        return False


def has_flush(hands):
    '''
    check if there is a pattern of flush in the hands;
    input type is a list of strings of any quantity '''

    table_suit = [i[0] for i in hands]
    for item in set(table_suit):
        if table_suit.count(item) >= 5:
            return item
    else:
        return False


def has_straight(hands):
    '''
    check if there is a pattern of straight in the hands;
    input type is a list of strings of any quantity '''

    table_digit = [value[i.strip(i[0])] for i in hands]
    table_digit = list(set(table_digit))
    # Set will sort the list of interger from low to high

    for i in range(len(table_digit)-4):
        if statistics.variance(table_digit[i:i+5]) == 2.5:
            return True
    else:
        if (max(table_digit) - min(table_digit) == 12) & (table_digit[1:4] ==
                                                          [3, 4, 5]):
            return '12345'
        else:
            return False


def evaluation(hands):
    '''return what the best hands are'''

    myhands_value = [value[i[1]] for i in hands]

    freq_dict = {}
    for i in set(myhands_value):
        freq_dict[i] = myhands_value.count(i)
    freq_list = sorted(freq_dict.values())

    flush_info = has_flush(hands)

    if flush_info:
        besthands = [i for i in hands if i[0] == flush_info]
        if has_straight(besthands):
            return 'straight flush'
        else:
            return 'flush'
    elif max(freq_list) == 4:
        return '4 of a kind'
    elif (max(freq_list) == 3) & (freq_list[-2] >= 2):
        return 'full house'
    elif has_straight(hands):
        return 'straight'
    elif (max(freq_list) == 3) & (freq_list[-2] < 2):
        return '3 of a kind'
    elif max(freq_list) == 2:
        if freq_list[-2] == 2:
            return 'two pairs'
        else:
            return 'one pair'
    else:
        return 'all singles'


def stats_distribution(hands):
    '''evaluation of your hands against the table 5 cards'''
    result = []
    for hand in hands:
        result.append(evaluation(hand))
    stats = {}
    for item in set(result):
        stats[item] = result.count(item)/(len(result))
    [print(f"{k:16}", f"{value:.2%}")
     for k, value in sorted(stats.items(), key=lambda x: x[1])]


def assess_hands(hands, tables=[], n_sim=6000):
    # pass your hands to see if you should play
    combo = hands + tables

    if len(combo) == 7:
        stats_distribution(combo)
    else:
        handsim = poker_simulation(n_sim, 7-len(combo))
        ph = [combo + hand for hand in handsim if check_unique(combo + hand)]
        print(len(ph))
        stats_distribution(ph)

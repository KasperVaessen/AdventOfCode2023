import math
import numpy as np
from collections import Counter
from functools import cmp_to_key

def get_val(card,extra=False):
    if card[0] == 'T':
        return 10
    elif card[0] == 'J' and not extra:
        return 11
    elif card[0] == 'J' and extra:
        return 1
    elif card[0] == 'Q':
        return 12
    elif card[0] == 'K':
        return 13
    elif card[0] == 'A':
        return 14
    else:
        return int(card[0])

def get_hand(hand):
    counter = Counter(hand)
    counter = counter.most_common()
    if counter[0][1] == 5:
        return 7
    elif counter[0][1] == 4:
        return 6
    elif counter[0][1] == 3 and counter[1][1] == 2:
        return 5
    elif counter[0][1] == 3:
        return 4
    elif counter[0][1] == 2 and counter[1][1] == 2:
        return 3
    elif counter[0][1] == 2:
        return 2
    else:
        return 1

def get_hand_joker(hand):
    counter1 = Counter(hand)

    if not 'J' in hand:
        return get_hand(hand)
    am_jokers = counter1['J']
    if am_jokers == 5:
        return 7
    
    counter1.pop('J')
    counter = counter1.most_common()

    if counter[0][1] + am_jokers == 5:
        return 7
    if counter[0][1] + am_jokers == 4:
        return 6
    for i in range(am_jokers):
        if counter[0][1] + am_jokers - i == 3 and counter[1][1] + i == 2:
            return 5
    if counter[0][1] + am_jokers == 3:
        return 4
    for i in range(am_jokers):
        if counter[0][1] + am_jokers - i == 2 and counter[1][1] + i == 2:
            return 5
    if counter[0][1] + am_jokers == 2:
        return 2
    else:
        return 1


def compare(hand1, hand2):
    h1 = hand1[0]
    h2 = hand2[0]
    
    val1 = get_hand(h1)
    val2 = get_hand(h2)

    if val1 > val2:
        return 1
    elif val1 < val2:
        return -1
    for i in range(5):
        if get_val(h1[i]) > get_val(h2[i]):
            return 1
        elif get_val(h1[i]) < get_val(h2[i]):
            return -1
    return 0

def compare_joker(hand1, hand2):
    h1 = hand1[0]
    h2 = hand2[0]
    
    val1 = get_hand_joker(h1)
    val2 = get_hand_joker(h2)

    if val1 > val2:
        return 1
    elif val1 < val2:
        return -1
    for i in range(5):
        if get_val(h1[i], extra=True) > get_val(h2[i], extra=True):
            return 1
        elif get_val(h1[i], extra=True) < get_val(h2[i], extra=True):
            return -1
    return 0
    


with open('7/input.txt', 'r') as f:
    input = [line.split() for line in f.read().split('\n')]

    input.sort(key=cmp_to_key(compare))
    input2 = input.copy()
    input2.sort(key=cmp_to_key(compare_joker))

    sum = 0
    sum2 = 0
    for i in range(len(input)):
        sum += int(input[i][1])*(i+1)
        sum2 += int(input2[i][1])*(i+1)

    print(sum, sum2)
    



    
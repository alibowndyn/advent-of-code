from collections import Counter
from functools import cmp_to_key


inp = open('../input.txt', 'r').read().splitlines()

strengths = {
    'A': 12, 'K': 11,
    'Q': 10, 'J':  9,
    'T':  8, '9':  7,
    '8':  6, '7':  5,
    '6':  4, '5':  3,
    '4':  2, '3':  1,
    '2':  0
}

hands = list()


for line in inp:
    hand, bid = line.split(' ')

    sort_key = int((s := ''.join(map(str, sorted(Counter(hand).values(), reverse=True)[:3]))) + ((3 - len(s)) * '0'))
    hands.append((hand, int(bid), sort_key))


def comp_hand(hand1, hand2):
    if hand1[2] != hand2[2]:
        return hand1[2] - hand2[2]

    for c1, c2 in zip(hand1[0], hand2[0]):
        if c1 != c2:
            return strengths[c1]  - strengths[c2]


print(sum([i*hand[1] for i,hand in enumerate(sorted(hands, key=cmp_to_key(comp_hand)), 1)]))

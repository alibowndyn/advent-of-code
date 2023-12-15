import re


inp = open('../input.txt', 'r').read().splitlines()

winning_nums, my_own_nums = set(), set()
cards = [1] * len(inp)


for i, card in enumerate(inp):
    parts = card.split('|')

    winning_nums = set( re.findall('\d+', parts[0])[1:] )
    my_own_nums  = set( re.findall('\d+', parts[1]) )

    num_of_copies = len( winning_nums.intersection(my_own_nums) )


    for copy_id in range(i + 1, i + num_of_copies + 1):
        cards[copy_id] += cards[i]


total_cards = sum(cards)
print(total_cards)

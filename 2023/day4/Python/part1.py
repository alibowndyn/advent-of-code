import re


inp = open('../input.txt', 'r').read().splitlines()

winning_nums, my_own_nums = set(), set()
total_points = 0


for card in inp:
    parts = card.split('|')

    winning_nums = set( re.findall('\d+', parts[0])[1:] )
    my_own_nums  = set( re.findall('\d+', parts[1]) )

    exponent = len( winning_nums.intersection(my_own_nums) ) - 1
    total_points += int(2 ** exponent)


print(total_points)

import re


inp = open('../input.txt', 'r').read().splitlines()

races = [map(int, re.findall('\d+', race)) for race in inp]
product = 1


for time, record_dist in zip(races[0], races[1]):
    time_to_travel = time - 1
    ways_to_win = 0

    for hold_time in range(1, time // 2 + 1):
        dist = hold_time * time_to_travel

        if dist > record_dist:
            ways_to_win += 2

        time_to_travel -= 1

    # if we win with the middle of the hold_time range
    # count it only once
    if (time % 2 == 0) and (time//2 * time_to_travel) > record_dist:
        ways_to_win -= 1


    if ways_to_win > 0:
        product *= ways_to_win


print(product)

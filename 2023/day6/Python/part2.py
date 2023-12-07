import re


inp = open('../input.txt', 'r').read().splitlines()

big_race = [int( re.search('\d+', race.replace(' ', '')).group() ) for race in inp]
time, record_dist = big_race[0], big_race[1]

time_to_travel = time - 1
ways_to_win = 0


for hold_time in range(1, time // 2 + 1):
    dist = hold_time * time_to_travel

    if dist > record_dist:
        ways_to_win += 2

    time_to_travel -= 1


if (time % 2 == 0) and (time//2 * time_to_travel) > record_dist:
    ways_to_win -= 1


print(ways_to_win)

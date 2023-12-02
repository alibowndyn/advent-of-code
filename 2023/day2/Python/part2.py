inp = open('../input.txt', 'r').read().split('\n')[:-1]

power_sum = 0


for line in inp:
    game = line.split(': ')
    list_of_cubes = game[1].split('; ')

    min_reds, min_greens, min_blues = 0, 0, 0


    for cubes in list_of_cubes:
        for cube in cubes.split(', '):
            reds   = int(cube[:-4]) if 'd' in cube else 0
            greens = int(cube[:-6]) if 'g' in cube else 0
            blues  = int(cube[:-5]) if 'b' in cube else 0

            min_reds   = max(min_reds,   reds)
            min_greens = max(min_greens, greens)
            min_blues  = max(min_blues,  blues)


    power_sum += min_reds * min_greens * min_blues


print(power_sum)
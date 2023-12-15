inp = open('../input.txt', 'r').read().split('\n')[:-1]

id_sum = 0


for line in inp:
    game = line.split(': ')
    list_of_cubes = game[1].split('; ')

    is_config_possible = True


    for cubes in list_of_cubes:
        for cube in cubes.split(', '):
            reds   = int(cube[:-4]) if 'd' in cube else 0
            greens = int(cube[:-6]) if 'g' in cube else 0
            blues  = int(cube[:-5]) if 'b' in cube else 0

            if (reds > 12 or greens > 13 or blues > 14):
                is_config_possible = False


    if is_config_possible:
        id_sum += int(game[0][5:])


print(id_sum)
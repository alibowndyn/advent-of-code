from collections import defaultdict
import itertools as it



def is_valid_coord(map_of_antennas: list[list[str]], coord) -> bool:
    l = len(map_of_antennas)
    ll = len(map_of_antennas[0])

    return (0 <= coord[0] < l) and (0 <= coord[1] < ll)


inp = open('../input.txt').read()

antennas = defaultdict(list)
antenna_map = [list(line) for line in inp.splitlines()]

for i in range(len(antenna_map)):
    for j, char in enumerate(antenna_map[i]):
        if char not in '.\n':
            antennas[char] += [(i, j)]


antinode_coords = []

for locations in antennas.values():
    for (ay, ax), (by, bx) in it.combinations(locations, r=2):
        dy, dx = ay - by, ax - bx

        match dy < 0, dx < 0:
            case False, False:    # top left
                antinode_coords += [(by - dy, bx - dx), (ay + dy, ax + dx)]

            case False, True:     # top right
                antinode_coords += [(by - dy, bx + abs(dx)), (ay + dy, ax - abs(dx))]

            case True, True:     # bottom right
                antinode_coords += [(by + abs(dy), bx + abs(dx)), (ay - abs(dy), ax - abs(dx))]

            case True, False:      # bottom left
                antinode_coords += [(by + abs(dy), bx - dx), (ay - abs(dy), ax + dx)]


valid_unique_antinode_coords = {coord for coord in antinode_coords if is_valid_coord(antenna_map, coord)}
print(len(valid_unique_antinode_coords))

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
        top, left = dy < 0, dx < 0

        for m in it.count():
            dy_m = dy * m
            dx_m = dx * m

            match top, left:
                case False, False:    # top left
                    c1, c2 = (by - dy_m, bx - dx_m), (ay + dy_m, ax + dx_m)

                case False, True:     # top right
                    c1, c2 = (by - dy_m, bx + abs(dx_m)), (ay + dy_m, ax - abs(dx_m))

                case True, True:      # bottom right
                    c1, c2 = (by + abs(dy_m), bx + abs(dx_m)), (ay - abs(dy_m), ax - abs(dx_m))

                case True, False:     # bottom left
                    c1, c2 = (by + abs(dy_m), bx - dx_m), (ay - abs(dy_m), ax + dx_m)

            if not is_valid_coord(antenna_map, c1) and not is_valid_coord(antenna_map, c2):
                break

            antinode_coords += [c1, c2]


valid_unique_antinode_coords = {coord for coord in antinode_coords if is_valid_coord(antenna_map, coord)}
print(len(valid_unique_antinode_coords))

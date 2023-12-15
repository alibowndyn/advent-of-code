from itertools import combinations


inp = open('../input.txt', 'r').read()
space = inp.splitlines()

row_len = inp.index('\n')
blank_row = '.' * row_len

blank_col_indices = []
blank_row_indices = []
galaxy_coords = []

# get the index of every blank column
for i, line in enumerate(space):
    if line == blank_row:
        blank_row_indices.append(i)

# get the index of every blank column
for i in range(row_len):
    is_col_blank = True

    for line in space:
        if line[i] == '#':
            is_col_blank = False
            break

    if not is_col_blank:
        continue
    else:
        blank_col_indices.append(i)


space = [list(line) for line in space]

for y, line in enumerate(space):
    for x, char in enumerate(line):
        if char == '#':
            # For every galaxy, we will offset that galaxy's (y, x) coordinate with the
            # number of blank rows & columns before it, times the expansion rate.
            y_offset = len( [i for i in blank_row_indices if y > i] ) * 999_999
            x_offset = len( [i for i in blank_col_indices if x > i] ) * 999_999

            galaxy_coords.append( (y + y_offset, x + x_offset) )


galaxy_pairs = combinations(galaxy_coords, 2)
sum = 0

for pair in galaxy_pairs:
    # |y2 - y1| + |x2 - x1|
    shortest_path = abs(pair[1][0] - pair[0][0]) + abs(pair[1][1] - pair[0][1])

    sum += shortest_path


print(sum)

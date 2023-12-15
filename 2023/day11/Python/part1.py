from itertools import combinations


inp = open('../input.txt', 'r').read()
space = inp.splitlines()

row_len = inp.index('\n')
blank_row = '.' * row_len

blank_col_indices = []
expanded_space = []
galaxy_coords = []


# after every blank row, add in another blank row
for line in space:
    expanded_space.append(line)

    if line == blank_row:
        expanded_space.append(blank_row)

# get the index of every blank column
for i in range(row_len):
    is_col_blank = True

    for line in expanded_space:
        if line[i] == '#':
            is_col_blank = False
            break

    if not is_col_blank:
        continue
    else:
        blank_col_indices.append(i)


# after every blank column, add in another blank column
for offset, idx in enumerate(blank_col_indices):
    for j, line in enumerate(expanded_space):
        expanded_space[j] = line[:idx + offset] + '.' + line[idx + offset:]


space = [list(line) for line in expanded_space]

for y, line in enumerate(expanded_space):
    for x, char in enumerate(line):
        if char == '#':
            galaxy_coords.append( (y, x) )


galaxy_pairs = combinations(galaxy_coords, 2)
sum = 0

for pair in galaxy_pairs:
    # |y2 - y1| + |x2 - x1|
    shortest_path = abs(pair[1][0] - pair[0][0]) + abs(pair[1][1] - pair[0][1])

    sum += shortest_path


print(sum)

dir_idx_offsets = [  # (x, y)
    [ ( 0, -1), ( 0, -2), ( 0, -3) ],  # up
    [ ( 1, -1), ( 2, -2), ( 3, -3) ],  # up right
    [ ( 1,  0), ( 2,  0), ( 3,  0) ],  # right
    [ ( 1,  1), ( 2,  2), ( 3,  3) ],  # down right
    [ ( 0,  1), ( 0,  2), ( 0,  3) ],  # down
    [ (-1,  1), (-2,  2), (-3,  3) ],  # down left
    [ (-1,  0), (-2,  0), (-3,  0) ],  # left
    [ (-1, -1), (-2, -2), (-3, -3) ],  # up left
]

def count_crosses_at_x(crossword: list[list[str]], xx, xy) -> int:
    count = 8

    for dir_offsets in dir_idx_offsets:
        for (x, y), c in zip(dir_offsets, "MAS"):
            if crossword[xy + y][xx + x] != c:
                count -= 1
                break

    return count

def pad_input(lines: list[str]) -> list[list[str]]:
    padded = [ ['.', '.'] + list(line) + ['.', '.'] for line in lines ]
    line_len = len(padded[0])

    padding_line = [['.'] * line_len ] * 2
    return padding_line + padded + padding_line



inp = open('../input.txt').read().splitlines()
crossword = pad_input(inp)

total_crosses = 0

for y, line in enumerate(crossword[2:-2], 2):  #
    for x, c in enumerate(line[2:-2], 2):      # skip the padding
        if c == 'X':
            total_crosses += count_crosses_at_x(crossword, x, y)

print(total_crosses)

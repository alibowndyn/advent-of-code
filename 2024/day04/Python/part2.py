'''
    Four possible ways an `X-MAS` can occur. It's an `X-MAS` shape
    when a diagonal pair of conrners don't match.

    M.M   S.S   M.S   S.M
    .A.   .A.   .A.   .A.
    S.S   M.M   M.S   S.M
'''
def is_x_mas(crossword: list[list[str]], ax, ay) -> bool:
    top_left     = crossword[ay - 1][ax - 1]
    top_right    = crossword[ay + 1][ax - 1]
    bottom_left  = crossword[ay - 1][ax + 1]
    bottom_right = crossword[ay + 1][ax + 1]

    # filter out any patterns where any of the corners are
    # either 'A', 'X' or my '.' pad character
    if any(corner in 'AX.' for corner in [top_left, top_right, bottom_left, bottom_right]):
        return False

    if top_left != bottom_right and top_right != bottom_left:
        return True

    return False

def pad_input(lines: list[str]) -> list[list[str]]:
    padded = [ ['.', '.'] + list(line) + ['.', '.'] for line in lines ]
    line_len = len(padded[0])

    padding_line = [['.'] * line_len ] * 2
    return padding_line + padded + padding_line



inp = open('../input.txt').read().splitlines()
crossword = pad_input(inp)

total_xmas = 0

for y, line in enumerate(crossword[2:-2], 2):  #
    for x, c in enumerate(line[2:-2], 2):      # skip the padding
        if c == 'A' and is_x_mas(crossword, x, y):
            total_xmas += 1

print(total_xmas)

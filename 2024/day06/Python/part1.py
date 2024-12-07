inp = open('../input.txt').read()

def pad_input(lines: list[str]) -> list[list[str]]:
    padded = [ ['x'] + list(line) + ['x'] for line in lines]
    line_len = len(padded[0])

    padding_line = [['x'] * line_len]
    return padding_line + padded + padding_line

def find_guard_pos(lab_map: str) -> tuple[int, int]:
    line_len = lab_map.index('\n') + 1
    guard_idx = lab_map.index('^')

    # adding +1 to account for the padding later
    return ((guard_idx // line_len) + 1, (guard_idx % line_len) + 1)



guard_y, guard_x = find_guard_pos(inp)
lab_map = pad_input(inp.splitlines())

# (y, x)          up    right    down    left
directions = [ (-1, 0), (0, 1), (1, 0), (0, -1) ]
curr_dir = directions[0]
curr_pos = lab_map[guard_y][guard_x]

num_obstacles_hit = 0
steps = set()

while (curr_pos != 'x'):
    if curr_pos != '#':
        steps.add((guard_y, guard_x))
    else:
        num_obstacles_hit += 1
        guard_y, guard_x = guard_y - curr_dir[0], guard_x - curr_dir[1]
        curr_dir = directions[num_obstacles_hit % 4]

    guard_y, guard_x = guard_y + curr_dir[0], guard_x + curr_dir[1]
    curr_pos = lab_map[guard_y][guard_x]


print(len(steps))

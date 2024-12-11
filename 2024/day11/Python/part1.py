def apply_rules(marks: list[str]) -> list[str]:
    new_marks = []

    for mark in marks:
        if mark == '0':
            new_marks.append('1')
        elif (l := len(mark)) % 2 == 0:
            left = mark[:l // 2]

            right = mark[l // 2:]
            right = right[:-1].lstrip('0') + right[-1] if right.startswith('0') else right

            new_marks += [left, right]
        else:
            new_marks.append(str( int(mark) * 2024 ))

    return new_marks


inp = open('../input.txt').read().split()


for _ in range(25):
    inp = apply_rules(inp)

print(len(inp))

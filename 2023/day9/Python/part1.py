inp = open('../input.txt', 'r').read().splitlines()

sum = 0


for line in inp:
    num_sequence = list( map(int, line.split(' ')) )
    next_num = 0

    while any(num_sequence):
        next_num += num_sequence[-1]
        num_sequence = [num_sequence[i] - num_sequence[i-1] for i in range(1, len(num_sequence))]

    sum += next_num


print(sum)

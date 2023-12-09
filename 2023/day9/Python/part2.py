inp = open('../input.txt', 'r').read().splitlines()

sum = 0


for line in inp:
    num_sequence = list( map(int, line.split(' ')) )
    sequence_list = []
    next_num = 0

    while any(num_sequence):
        sequence_list.append(num_sequence)
        num_sequence = [num_sequence[i] - num_sequence[i-1] for i in range(1, len(num_sequence))]

    for i in range(len(sequence_list) - 1, -1, -1):
        next_num = sequence_list[i][0] - next_num

    sum += next_num


print(sum)

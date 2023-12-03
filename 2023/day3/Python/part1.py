inp = open('../input.txt', 'r').read().splitlines()


row_len = len(inp[0])
offsets = [1, row_len+1, row_len, row_len-1, -1, -row_len-1, -row_len, -row_len+1]

inp = ''.join(inp)
inp_len = len(inp)

is_num_sequence = False
is_part_number = False

part_num_sum = 0
char, num = '', ''


for i in range(inp_len):
    char = inp[i]

    if char.isdigit():
        # the indices of the characters surrounding our digit
        probe_indices = [i + offset for offset in offsets]

        # check every character around our digit in clockwise
        # direction, starting from the right
        for k, probe_idx in enumerate(probe_indices):
            if probe_idx >= 0 and probe_idx < inp_len:

                num = num if is_num_sequence else char
                probe_chr = inp[probe_idx]

                if probe_chr.isdigit():
                    # if the char to the right is a number
                    if k == 0:
                        is_num_sequence = True
                        num += probe_chr
                else:
                    if probe_chr != '.':
                        is_part_number = True
                        continue
    else:
        # if there was a part number before the current character
        if is_part_number:
            part_num_sum += int(num)
            is_part_number = False

        num = ''
        is_num_sequence = False


print(part_num_sum)

inp = open('../input.txt', 'r').read().splitlines()


row_len = len(inp[0])
offsets = [1, row_len+1, row_len, row_len-1, -1, -row_len-1, -row_len, -row_len+1]

inp = ''.join(inp)
inp_len = len(inp)

gear_nums = set()
gear_ratio_sum = 0


for i in range(inp_len):
    probe_indices = [i + offset for offset in offsets]
    gear_nums = set()
    char = inp[i]

    if char == '*':
        # look around the '*' searching for digits
        for probe_idx in probe_indices:
            probe_chr = inp[probe_idx]

            if probe_chr.isdigit():
                # this substring will contain the whole number
                # that touches the '*'
                slice_with_num = inp[probe_idx - 2:probe_idx + 3]

                # modify the slice so it can only contain one sequence of numbers
                if not slice_with_num[1].isdigit():
                    # e.g. '2.517'   '2*967'   '.*338'
                    slice_with_num = slice_with_num[2:]

                if not slice_with_num[-2].isdigit():
                    # e.g. '523.7'   '602*9'   '963*.'
                    slice_with_num = slice_with_num[:-2]

                # we don't have to worry about other symbols appearing
                # next to our number in the slice, since a number
                # can only have 1 type of symbol touching it,
                # so now it's easy to extract the number from the slice
                gear_num = int( slice_with_num.strip('.') )
                gear_nums.add(gear_num)

        if len(gear_nums) == 2:
            gear_ratio_sum += gear_nums.pop() * gear_nums.pop()


print(gear_ratio_sum)

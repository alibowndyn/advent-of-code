inp = open('../input.txt', 'r').read().split('\n\n')

sum = 0


for pattern in inp:
    rows    = pattern.count('\n')
    row_len = pattern.find('\n')
    is_horizontal = False
    v_reflection = 0
    h_reflection = 0


    for i in range(rows):
        above = pattern[i     * (row_len+1):i     * (row_len+1) + row_len]
        below = pattern[(i+1) * (row_len+1):(i+1) * (row_len+1) + row_len]

        if above == below:
            is_horizontal = True
            left_i, right_i =  i-1, i+2

            while (left_i > -1) and (right_i < rows + 1):
                above = pattern[left_i  * (row_len+1):left_i  * (row_len+1) + row_len]
                below = pattern[right_i * (row_len+1):right_i * (row_len+1) + row_len]

                if above != below:
                    is_horizontal = False

                left_i  -= 1
                right_i += 1

            if is_horizontal:
                h_reflection = i + 1

                if (left_i == -1) or (right_i == rows):
                    break


    if not is_horizontal:
        for i in range(row_len):
            left  = pattern[i  ::row_len + 1]
            right = pattern[i+1::row_len + 1]

            if left == right:
                left_i, right_i =  i-1, i+2

                while (left_i > -1) and (right_i < row_len):
                    left  = pattern[left_i ::row_len + 1]
                    right = pattern[right_i::row_len + 1]

                    if left != right:
                        break

                    left_i  -= 1
                    right_i += 1

                v_reflection = i + 1

                if (left_i == -1) or (right_i == row_len-1):
                    break


    sum += v_reflection + h_reflection * 100


print(sum)

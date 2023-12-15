import re


inp = open('../input.txt', 'r').readlines()

num_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
pattern = '\d|one|two|three|four|five|six|seven|eight|nine'
calib_sum = 0


for line in inp[:-1]:
    matched_nums = re.findall(pattern, line)
    first = matched_nums[0]
    last = matched_nums[-1]


    if (matched_nums[0] in num_words):
        first = str( num_words.index(matched_nums[0]) + 1 )

    if (matched_nums[-1] in num_words):
        possible_last_num = matched_nums[-1]

        while True:
            next_possible_match_idx = line.rfind(possible_last_num) + len(possible_last_num) - 1
            match = re.match(pattern, line[next_possible_match_idx:])

            if not match:
                break

            possible_last_num = match.group(0)

        last = str( num_words.index(possible_last_num) + 1 )


    calibration_value = first + last
    calib_sum += int(calibration_value)


print(calib_sum)
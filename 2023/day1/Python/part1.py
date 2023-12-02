import re


inp = open('../input.txt', 'r').readlines()

calib_sum = 0


for line in inp[:-1]:
    nums = re.findall('\d', line)

    calibration_value = nums[0] + nums[-1]
    calib_sum += int(calibration_value)


print(calib_sum)
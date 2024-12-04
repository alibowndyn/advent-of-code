inp = open('../input.txt').readlines()



count = 0

for nums in [list(map(int, line.split())) for line in inp]:
    n = nums[0]
    inc = False
    dec = False
    is_safe = True

    for num in nums[1:]:
        diff = abs(n - num)

        if diff < 1 or diff > 3:
            is_safe = False
            break

        if num < n:
            if inc:
                inc = False
                break
            dec = True
        else:
            if dec:
                dec = False
                break
            inc = True

        n = num

    if (inc or dec) and is_safe:
        count += 1

print(count)

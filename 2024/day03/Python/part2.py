import re



inp = open('../input.txt').read()

# remove `don't()` and everything until the next `do()`,
# this way we're removing all disabled mul instuctions
disabled_mul_removed = re.sub(r"don't\(\)([\s\S]*?do\(\)|.*)", "", inp)

mul_matches = re.findall(r'mul\((\d{,3}),(\d{,3})\)', disabled_mul_removed)

print(sum(map(lambda x: int(x[0]) * int(x[1]), mul_matches)))
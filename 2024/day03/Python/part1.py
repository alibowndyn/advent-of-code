import re



inp = open('../input.txt').read()

mul_matches = re.findall(r'mul\((\d{,3}),(\d{,3})\)', inp)

print(sum(map(lambda x: int(x[0]) * int(x[1]), mul_matches)))

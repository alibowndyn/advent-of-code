inp = open('../input.txt').readlines()
total_distance = 0
group1, group2 = [], []

for (id1, id2) in [line.split('   ') for line in inp]:
    group1.append(int(id1))
    group2.append(int(id2))

for (id1, id2) in zip(sorted(group1), sorted(group2)):
    total_distance += abs(id1 - id2)

print(total_distance)
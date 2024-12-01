inp = open('../input.txt').readlines()
similarity_score = 0
group1, group2 = [], []

for (id1, id2) in [line.split() for line in inp]:
    group1.append(int(id1))
    group2.append(int(id2))

for id_to_count in group1:
    similarity_score += id_to_count * group2.count(id_to_count)

print(similarity_score)
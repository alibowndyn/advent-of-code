inp = open('../input.txt', 'r').read()

seeds = list( map(int, inp[7:inp.index('\n')].split(' ')) )
maps = [mapping.splitlines()[1:] for mapping in inp.split('\n\n')]

locations = list()
mapped = 0


for seed in seeds:
    mapped = seed

    for map_ranges in maps:
        for map_range in map_ranges:
            dst, src, offset = map(int, map_range.split(' '))

            if src <= mapped <= src + offset:
                mapped = mapped + (dst - src)
                break

    locations.append(mapped)


print(min(locations))

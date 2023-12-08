inp = open('../input.txt', 'r').read()

directions = inp[:inp.index('\n')]
nodes = inp[len(directions) + 2:].splitlines()

# a list containing only the nodes' names
node_names = [node[:3] for node in nodes]

for i, node in enumerate(nodes):
    node_idx  = node_names.index(node[  : 3])
    left_idx  = node_names.index(node[ 7:10])
    right_idx = node_names.index(node[12:15])

    nodes[node_idx] = (left_idx, right_idx)


current_node_idx = node_names.index('AAA')
end_node_index   = node_names.index('ZZZ')
steps = 0


while (current_node_idx != end_node_index):
    for d in directions:
        steps += 1

        if d == 'L':
            current_node_idx = nodes[current_node_idx][0]
        else:
            current_node_idx = nodes[current_node_idx][1]


print(steps)

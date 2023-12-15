import math


inp = open('../input.txt', 'r').read()

directions = inp[:inp.index('\n')]
nodes = inp[len(directions) + 2:].splitlines()

# a list containing only the nodes' names
node_names = [node[:3] for node in nodes]

# For every node, replace all 3 node names with their indices in the
# node_names list. With this, we can implicitly store the 1st node
# name as the index where that node is in the nodes list.
for i, node in enumerate(nodes):
    node_idx  = node_names.index(node[  : 3])
    left_idx  = node_names.index(node[ 7:10])
    right_idx = node_names.index(node[12:15])

    nodes[node_idx] = (left_idx, right_idx)


# the initial values are the "start nodes" (nodes ending in 'A')
current_node_idxs = [i for i in range(len(node_names)) if node_names[i].endswith('A')]

steps_per_start_nodes = []
found_all_end_nodes = False
steps = 0


while (not found_all_end_nodes):
    for d in directions:
        steps += 1

        # for every one of our starting nodes, with every
        # iteration, we move to the next node and check
        # whether we've reached an end-node for that node
        for i, node_idx in enumerate(current_node_idxs):
            # get the next node for the current node
            current_node_idxs[i] = nodes[node_idx][0 if (d == 'L') else 1]

            # if the next node is an end-node,
            # save the steps required to get there
            if node_names[current_node_idxs[i]].endswith('Z'):
                steps_per_start_nodes.append(steps)

    if ( len(steps_per_start_nodes) == len(current_node_idxs) ):
        found_all_end_nodes = True


# the steps required for the start-nodes to simultaneously reach
# their end-nodes is the lowest common multiple of the steps
# taken for every start-node to reach their respective end-node
print(math.lcm(*steps_per_start_nodes))

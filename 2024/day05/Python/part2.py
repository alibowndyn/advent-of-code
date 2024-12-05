ordering_rules, updates = open('../input.txt').read().split('\n\n')

ordering_rules = [(int(x[0]), int(x[1])) for rule in ordering_rules.splitlines() if (x := rule.split('|'))]
updates = [list(map(int, update.split(','))) for update in updates.splitlines()]



fixed_order_updates = dict()

for i, update in enumerate(updates):
    for j in range(len(update)):
        for page in update[j+1:]:
            if (page, update[j]) in ordering_rules:
                page_idx = update.index(page)

                # fix the order by swapping
                update[page_idx], update[j] = update[j], update[page_idx]

                # this assignment is just a reference copy, so the change in order
                # by swapping will be reflected in the values of this dictionary
                fixed_order_updates[i] = update


print(sum(update[len(update) // 2] for update in fixed_order_updates.values()))

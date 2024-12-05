ordering_rules, updates = open('../input.txt').read().split('\n\n')

ordering_rules = [(int(x[0]), int(x[1])) for rule in ordering_rules.splitlines() if (x := rule.split('|'))]
updates = [list(map(int, update.split(','))) for update in updates.splitlines()]


# i'm not returning False explicitly because None will
# evaluate to False in an if statement anyway
def is_update_order_wrong(update: list[int]) -> bool | None:
    for i in range(len(update)):
        for page in update[i+1:]:
            if (page, update[i]) in ordering_rules:
                return True


print(sum(update[len(update) // 2] for update in updates if not is_update_order_wrong(update)))

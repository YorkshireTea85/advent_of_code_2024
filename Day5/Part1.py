# Open input file
with open("Day5/Input.txt", 'r') as file:
    

    lines = file.readlines()

    page_num_sum = 0
    order_rules = []
    updates = []

    for line in lines:
        if "|" in line:
            rule_split = line.strip().split("|")
            order_rules.append((rule_split[0], rule_split[1]))
        elif "," in line:
            updates.append([number for number in line.strip().split(",")])

    for update in updates:
        is_correctly_ordered = True
        for rule in order_rules:
            rule_left, rule_right = rule
            if rule_left in update and rule_right in update:
                page_right_index = update.index(rule_right)
                page_left_index = update.index(rule_left)
                for page in update:
                    if page == rule_left and page_left_index > page_right_index:
                        is_correctly_ordered = False

        if is_correctly_ordered: 
            page_num_sum += int(update[len(update)//2])

    print(page_num_sum)
            
del file
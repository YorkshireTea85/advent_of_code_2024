# Open input file
with open("Day5/Input.txt", 'r') as file:
    
    lines = file.readlines()

    page_num_sum = 0
    order_rules = []
    order_validation = {}
    updates = []

    # Function to check if update is correctly ordered
    def check_update_order(update, rules):
        is_correctly_ordered = True

        for rule in order_rules:
            rule_left, rule_right = rule
            if rule_left in update and rule_right in update:
                page_right_index = update.index(rule_right)
                page_left_index = update.index(rule_left)
                for page in update:
                    if page == rule_left and page_left_index > page_right_index:
                        is_correctly_ordered = False
        return is_correctly_ordered

    # Extract rules and update from main text
    for line in lines:
        if "|" in line:
            rule_split = line.strip().split("|")
            order_rules.append((rule_split[0], rule_split[1]))
        elif "," in line:
            updates.append([number for number in line.strip().split(",")])

    # Create dictionary of page numbers and their respective preceding and suceeding pages
    for rule in order_rules:
        if rule[0] not in order_validation.keys():
            order_validation[rule[0]] = {"preceding_pages": [], "succeeding_pages": [rule[1]]}
        else:
            order_validation[rule[0]]["succeeding_pages"].append(rule[1])
        
        if rule[1] not in order_validation.keys():
            order_validation[rule[1]] = {"preceding_pages": [rule[0]], "succeeding_pages": []}
        else:
            order_validation[rule[1]]["preceding_pages"].append(rule[0])

    for update in updates:
        
        if check_update_order(update, order_rules) == True:
            continue
        
        update_check = False

        while update_check == False:
            
            for page in update:

                # Define valid preceeding and succeding pages for current selected page in accordance with rules
                valid_preceding_pages = order_validation[page]["preceding_pages"]
                valid_succeeding_pages = order_validation[page]["succeeding_pages"]

                current_preceding_pages = []
                current_succeeding_pages = []

                page_index = update.index(page)

                # Define current preceeding and succeding page state for current selected page
                for page2 in update:
                    if update.index(page2) < page_index:
                        current_preceding_pages.append(page2)
                    elif update.index(page2) > page_index:
                        current_succeeding_pages.append(page2)
    
                for cur_suc_page in current_succeeding_pages:
                    suc_page_index = update.index(cur_suc_page)
                    if cur_suc_page in valid_preceding_pages:
                        removed_page = update.pop(suc_page_index)
                        update.insert(page_index,removed_page)

                for cur_prec_page in current_preceding_pages:
                    prec_page_index = update.index(cur_prec_page)
                    if cur_prec_page in valid_succeeding_pages:
                        removed_page = update.pop(prec_page_index)
                        update.insert(page_index+1,removed_page)

                update_check = check_update_order(update, order_rules)
                
                if update_check:
                    page_num_sum += int(update[len(update)//2])
                    break

    print(page_num_sum)
            
del file
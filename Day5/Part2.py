xmas_count = 0

# Open input file
with open("Day5/Test_Input.txt", 'r') as file:
    

    lines = file.readlines()

    grid = [[letter for letter in line.strip()] for line in lines]

    
    for i, row in enumerate(grid):
        for j, letter in enumerate(row):
            if letter == "A":
                # Ensure the letter is not on the boundary of the grid
                if (i <= 0 or i >= len(grid)-1) or (j <= 0 or j >= len(row)-1):
                    pass
                else:
                    tl_to_br = f"{grid[i-1][j-1]}{grid[i][j]}{grid[i+1][j+1]}"
                    tr_to_bl = f"{grid[i-1][j+1]}{grid[i][j]}{grid[i+1][j-1]}"

                    if (tl_to_br == "MAS" or tl_to_br == "SAM") and (tr_to_bl == "MAS" or tr_to_bl == "SAM"):
                        xmas_count += 1

    print(xmas_count)
        
del file# Open input file
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
                        removed_page = update.pop(page_left_index)
                        update.insert(page_right_index, removed_page)
                        is_correctly_ordered = False

        if is_correctly_ordered == False:  
            page_num_sum += int(update[len(update)//2])

    print(page_num_sum)
            
del file
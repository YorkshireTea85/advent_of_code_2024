safe_report_count = 0

def report_check(report):

    score = int()
    increasing = None
    for i, level in enumerate(report):
        if i == 0:
            continue

        previousLevel = report[i - 1]
        currentLevel = report[i]

        score = currentLevel - previousLevel
        if score < -3 or score > 3 or score == 0:
            return False
        if increasing == True and score < 0:
            return False
        if increasing == False and score > 0:
            return False
        
        if score < 0:
            increasing = False
        else: increasing = True
        
    return True
                

# Open input file
with open("Day2/Input.txt", 'r') as file:

    # Create list of reports (as Strings) with whitespace and newlines removed
    reports = [[int(level) for level in line.rstrip().split()] for line in file.readlines()]

    # Loop through each report
    for index, report in enumerate(reports):
        direction = "none"
        safe_lvl_diff = range(1,4)
            
        is_safe = report_check(report)

        if is_safe == False:
            validation_log = []
            for i in range(len(report)):
                removed_value = report.pop(i)
                validation_log.append(report_check(report))
                report.insert(i, removed_value)
            
            if validation_log.count(True) >= 1:
                is_safe = True
        
        if is_safe:
            safe_report_count += 1

del file

print(safe_report_count)
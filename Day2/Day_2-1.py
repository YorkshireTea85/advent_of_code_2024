safe_report_count = 0

# Open input file
with open("Day2/Day_2-1_Input.txt", 'r') as file:

    # Create list of reports (as Strings) with whitespace and newlines removed
    reports = [[int(level) for level in line.rstrip().split()] for line in file.readlines()]

    # Loop through each report
    for report in reports:
        direction = "none"
        is_safe = True
        safe_lvl_diff = range(1,4)

        # Calculate direction from first two digits
        if report[0] < report[1]:
            direction = "incr"
        elif report[0] > report[1]:
            direction  = "decr"
        else:
            direction = "none"

        # Loop through each level
        for i in range(len(report)-1):
            # Apply safety check per direction
            match direction:
                case "incr":
                    if report[i] > report[i+1] or report[i+1] - report[i] not in safe_lvl_diff:
                        is_safe = False

                case "decr":
                    if report[i] < report[i+1] or report[i] - report[i+1] not in safe_lvl_diff:
                        is_safe = False

                case "none":
                    is_safe = False
        
        if is_safe:
            safe_report_count += 1



del file

print(safe_report_count)    
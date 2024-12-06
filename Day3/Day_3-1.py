import re

result = 0

# Open input file
with open("Day3/Day_3-1_Input.txt", 'r') as file:
    

    corrupted_memory = file.read()
    valid_commands = re.findall("mul\(([0-9]+),([0-9]+)\)",corrupted_memory)
    
    for command in valid_commands:
        result += int(command[0]) * int(command[1])

    print(result)

del file
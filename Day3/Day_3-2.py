import re

result = 0

# Open input file
with open("Day3/Day_3-2_Input.txt", 'r') as file:
    
    valid_commands = []

    corrupted_memory = file.read()

    split_by_dont = re.split("don't\(\)",corrupted_memory)

    for i, memory_string in enumerate(split_by_dont):
        if i == 0:
            valid_command_extract = re.findall("mul\(([0-9]+),([0-9]+)\)",memory_string)
            # print(valid_command_extract)
            valid_commands += valid_command_extract
        else:
            split_by_do = re.split("do\(\)",memory_string)
            
            for i, memory_string in enumerate(split_by_do):
                if i > 0:
                    valid_command_extract = re.findall("mul\(([0-9]+),([0-9]+)\)",memory_string)
                    valid_commands += valid_command_extract
    
    for command in valid_commands:
        result += int(command[0]) * int(command[1])

    print(result)

del file
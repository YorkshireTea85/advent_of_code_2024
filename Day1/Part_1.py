left_list = []
right_list = []
id_difference = 0

with open("Day1/Input.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        line_split = line.split()
        left_list.append(int(line_split[0]))
        right_list.append(int(line_split[1]))

del file

left_list.sort()
right_list.sort()

for i in range(len(left_list)):
    id_difference += abs(left_list[i] - right_list[i])

print(id_difference)    
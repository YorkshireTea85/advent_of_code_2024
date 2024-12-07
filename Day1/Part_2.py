left_list = []
right_list = []
similarity_score = 0

with open("Day1/Input.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        line_split = line.split()
        left_list.append(int(line_split[0]))
        right_list.append(int(line_split[1]))

del file

for id_l in left_list:
    similarity_count = 0
    for id_r in right_list:
        if id_l == id_r:
            similarity_count += 1
    similarity_score += id_l * similarity_count
    

print(similarity_score)    
word_count = 0

def match_letter(current_letter_coord, current_letter, prev_coord="",prev_letters=""):
    
    col, row = current_letter_coord
    word_count = 0
    bounding_coord = [
        (col-1,row-1), # Above Left
        (col-1,row), # Above Centre
        (col-1,row+1), # Above Right
        (col,row-1), # Left
        (col,row+1), # Right
        (col+1,row-1), # Below Left
        (col+1,row), # Below Centre
        (col+1,row+1), # Below Right
    ]

    if current_letter == "X" and prev_letters == "":
        for coord in bounding_coord:
            if (coord[0] < 0 or coord[0] > len(grid)-1) or (coord[1] < 0 or coord[1] > len(grid[0])-1):
                pass
            else:
                word_count += match_letter(coord,grid[coord[0]][coord[1]],prev_coord=(current_letter_coord),prev_letters="X")
    
    if current_letter == "M" and prev_letters == "X":
        col_diff = prev_coord[0] - current_letter_coord[0]
        row_diff = prev_coord[1] - current_letter_coord[1]

        coord = (current_letter_coord[0] - col_diff, current_letter_coord[1] - row_diff)

        if (coord[0] < 0 or coord[0] > len(grid)-1) or (coord[1] < 0 or coord[1] > len(grid[0])-1):
            pass
        else:
            return match_letter(coord,grid[coord[0]][coord[1]],prev_coord=(current_letter_coord),prev_letters="XM")

    if current_letter == "A" and prev_letters == "XM":
        col_diff = prev_coord[0] - current_letter_coord[0]
        row_diff = prev_coord[1] - current_letter_coord[1]

        coord = (current_letter_coord[0] - col_diff, current_letter_coord[1] - row_diff)

        if (coord[0] < 0 or coord[0] > len(grid)-1) or (coord[1] < 0 or coord[1] > len(grid[0])-1):
            pass
        else:
            return match_letter(coord,grid[coord[0]][coord[1]],prev_coord=(current_letter_coord),prev_letters="XMA")        

    if current_letter == "S" and prev_letters == "XMA":
        return 1
    
    return word_count

# Open input file
with open("Day4/Day_4-1_Input.txt", 'r') as file:
    

    lines = file.readlines()

    grid = [[letter for letter in line.strip()] for line in lines]

    
    for i, row in enumerate(grid):
        for j, letter in enumerate(row):
            word_count += match_letter((i,j),letter)

    print(word_count)
    
    # print(match_letter((4,6),"X"))
    # print("")
    # for row in grid:
    #      print(row)
        
del file
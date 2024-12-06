xmas_count = 0

# Open input file
with open("Day4/Day_4-1_Input.txt", 'r') as file:
    

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
        
del file
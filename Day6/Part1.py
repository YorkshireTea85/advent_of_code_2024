guard_loc = []
guard_dir = "N"
direction_change = {
    "N":"E",
    "E":"S",
    "S":"W", 
    "W":"N"
    }
guard_move = {
    "N":(-1,0),
    "E":(0,1),
    "S":(1,0), 
    "W":(0,-1)
}
guard_symbol = {
    "N":"^",
    "E":">",
    "S":"v", 
    "W":"<"
}
positions = 0

# Function to print guard map
def print_map():
    for row in guard_map:
        print(row)

# Function to check which direction is clear and return next guard location and direction
def next_move(guard_loc, guard_dir):
    direction = guard_dir
    is_loc_valid = False

    while True:

        # Check current guard direction, if next move is valid and if not change direction.
        match direction:
            case "N":
                next_move_loc = [guard_loc[0] + guard_move[direction][0], guard_loc[1] + guard_move[direction][1]]
                if next_move_loc[0] < 0:
                    return next_move_loc, direction
                elif guard_map[next_move_loc[0]][next_move_loc[1]] != "#":
                    return next_move_loc, direction
                else:
                    direction = "E"
            case "E":
                next_move_loc = [guard_loc[0] + guard_move[direction][0], guard_loc[1] + guard_move[direction][1]]
                if next_move_loc[1] > len(guard_map[0])-1:
                    return next_move_loc, direction
                elif guard_map[next_move_loc[0]][next_move_loc[1]] != "#":
                    return next_move_loc, direction
                else:
                    direction = "S"
            case "S":
                next_move_loc = [guard_loc[0] + guard_move[direction][0], guard_loc[1] + guard_move[direction][1]]
                if next_move_loc[0] > len(guard_map)-1:
                    return next_move_loc, direction
                elif guard_map[next_move_loc[0]][next_move_loc[1]] != "#":
                    return next_move_loc, direction
                else:
                    direction = "W"
            case "W":
                next_move_loc = [guard_loc[0] + guard_move[direction][0], guard_loc[1] + guard_move[direction][1]]
                if next_move_loc[1] < 0:
                    return next_move_loc, direction
                elif guard_map[next_move_loc[0]][next_move_loc[1]] != "#":
                    return next_move_loc, direction
                else:
                    direction = "N"


# Open input file
with open("Day6/Input.txt", 'r') as file:
    
    guard_map = []

    lines = file.readlines()

    # Create guard map
    for i, line in enumerate(lines):
        row = []
        for j, char in enumerate(line.strip()):
            row.append(char)
            if char == "^":
                guard_loc = [i,j]
        guard_map.append(row)

    # Move the guard until out of bounds of guard map
    while True:
        # Move guard
        guard_next_move = next_move(guard_loc, guard_dir)

        # Get details of guard next move
        guard_dir = guard_next_move[1]
        guard_x = guard_next_move[0][1]
        guard_y = guard_next_move[0][0]

        # Mark guard previous location and end loop if guard out of bounds of map
        if (guard_x < 0 or guard_x > len(guard_map[0])-1) or (guard_y < 0 or guard_y > len(guard_map)-1):
            guard_map[guard_loc[0]][guard_loc[1]] = "X"
            break
        else:
            # Mark guard previous location and move guard symbol to new location
            guard_map[guard_loc[0]][guard_loc[1]] = "X"
            guard_loc = [guard_y, guard_x]
            guard_map[guard_loc[0]][guard_loc[1]] = guard_symbol[guard_dir]

    # Count all distinct guard locations
    for i in range(len(guard_map)):
        for j in range(len(row)):
            if guard_map[i][j] == "X":
                positions += 1

    #Print guard map and count of distinct locations            
    print_map()
    print(positions)
del file
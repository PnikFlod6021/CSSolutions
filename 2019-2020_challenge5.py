import random
import numpy as np
obstacles = ['#', '^']
def create_grid(grid_size):
    rows, cols = (grid_size + 2, grid_size + 2)
    grid = [["O"]*cols]*rows
    grid = np.array(grid)
    grid[:, [0, -1]] = "#"
    grid[[0, -1], :] = "#"
    create_obstacles(grid, grid_size)
    setrobotpos(grid, grid_size)
    setendpos(grid, grid_size)
    return (grid)
def create_obstacles(grid, grid_size):
    num_obstacles = 0
    while (num_obstacles <= grid_size - 1):
        obstacle_x = random.randint(0, grid_size - 1)
        obstacle_y = random.randint(0, grid_size - 1)
        if grid[obstacle_x][obstacle_y] != "#":
            grid[obstacle_x][obstacle_y] = random.choice(obstacles)
            num_obstacles += 1
        else:
            continue
    return grid
def setrobotpos(grid, grid_size):
    while True:
        x = random.randint(0, grid_size)
        y = random.randint(0, grid_size)
        if grid[x][y] == "O":
            grid[x][y] = "R"
            break
        else:
            continue
    return grid
def setendpos(grid, grid_size):
    while True:
        x = random.randint(0, grid_size)
        y = random.randint(0, grid_size)
        if grid[x][y] == "O":
            grid[x][y] = "E"
            break
        else:
            continue
    return grid
def getrobotpos(grid, grid_size):
    start_x = 0
    start_y = 0
    for i in range(grid_size + 1):
        for j in range(grid_size + 1):
            if grid[i][j] == "R":
                start_x = i
                start_y = j
                return (start_x, start_y)
def move_robot(grid, grid_size):
    x,y = getrobotpos(grid, grid_size)
    direction = input("Enter a direction: Left, Right, Up, Down").lower()
    if direction == "up":
        grid[x][y] = "O"
        x -= 1
    if direction == "down":
        grid[x][y] = "O"
        x +=1
    if direction == "left":
        grid[x][y] = "O"
        y-=1
    if direction == "right":
        grid[x][y] = "O"
        y += 1
    else:
        print("Invalid Direction")
    if grid[x][y] not in obstacles and grid[x][y] != "E":
        grid[x][y] = "R"
        return (grid)
    elif grid[x][y] in obstacles:
        print("YOU LOSE")
    else:
        print("YOU WON")
def main():
    while True:
        print("Calling Mr. Roboto!")
        print("R- Robot Starting Position")
        print("E- End Position")
        print("# - Wall")
        print("^ - Spike")
        size = int(input("Enter a size for your grid (2-10 inclusive)"))
        try:
            size = int(size)
            if size > 10 or size < 2:
                print("Invalid Size")
                main()
            else:
                break
        except ValueError:
            print("Invalid Input")
            main()
    grid = create_grid(size)
    print(grid)
    while True:
        try:
            print(move_robot(grid, size))
        except TypeError:
            print("")
            break
main()

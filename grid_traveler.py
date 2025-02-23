def grid_traveler(row: int, column: int) -> int:
    if row == 1 and column == 1:
        return 1
    if row == 0 or column == 0:
        return 0
    return grid_traveler(row - 1, column) + grid_traveler(row, column - 1)

def main()-> None:
    grid = (2,3)

    no_ways = grid_traveler(row=grid[0], column= grid[1])
    print(f"Number of ways to travel from top left to bottom right in a {grid[0]} by {grid[1]} is {no_ways}")

if __name__ =="__main__":
    main()
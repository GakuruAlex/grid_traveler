def grid_traveler(row: int, column: int) -> int:
    if row == 1 and column == 1:
        return 1
    if row == 0 or column == 0:
        return 0
    return grid_traveler(row - 1, column) + grid_traveler(row, column - 1)

def mem_grid_traveler(row: int, column: int, memo = {(1,1): 1}):
    if row == 0 or column == 0:
        return 0
    if (row,column) in memo:
        return memo[(row, column)]
    no_rows = mem_grid_traveler(row - 1, column, memo)
    no_columns = mem_grid_traveler(row, column - 1)
    memo[(row, column)] = no_rows + no_columns
    memo[(column, row)] = no_rows + no_columns
    return memo[(row, column)]

def main()-> None:
    grid = (2, 3)

    no_ways = grid_traveler(row=grid[0], column= grid[1])
    print(f"Number of ways to travel from top left to bottom right in a {grid[0]} by {grid[1]} is {no_ways}")

    no_ways_with_mem = mem_grid_traveler(row=18, column= 18)
    print(f"Number of ways to travel from top left to bottom right in a {grid[0]} by {grid[1]} is {no_ways_with_mem}")

if __name__ =="__main__":
    main()
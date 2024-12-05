import sys
MATCH = "XMAS"

def horizontal(i, j, grid):
    total = 0
    if j+3 < len(grid[i]):
        total += 1 if grid[i][j:j+4] == MATCH else 0
    if j-3 >= 0:
        total += 1 if grid[i][j-3:j+1] == MATCH[::-1] else 0
    return total

def vertical(i, j, grid):
    total = 0
    if i+3 < len(grid):
        total += 1 if grid[i][j] + grid[i+1][j] + grid[i+2][j] + grid[i+3][j] == MATCH else 0
    if i -3 >= 0:
        total += 1 if grid[i][j] + grid[i-1][j] + grid[i-2][j] + grid[i-3][j] == MATCH else 0
    return total

def diag(i, j, grid):
    total = 0
    if i + 3 < len(grid) and j + 3 < len(grid[i]):
        total += 1 if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] + grid[i+3][j+3] == MATCH else 0
    
    if i + 3 < len(grid) and j - 3 >= 0:
        total += 1 if grid[i][j] + grid[i+1][j-1] + grid[i+2][j-2] + grid[i+3][j-3] == MATCH else 0

    if i - 3 >= 0  and j + 3 < len(grid[i]):
        total += 1 if grid[i][j] + grid[i-1][j+1] + grid[i-2][j+2] + grid[i-3][j+3] == MATCH else 0
    
    if i - 3 >= 0 and j - 3 >= 0:
        total += 1 if grid[i][j] + grid[i-1][j-1] + grid[i-2][j-2] + grid[i-3][j-3] == MATCH else 0

    return total
def test(i, j, grid):
    return horizontal(i, j, grid) + vertical(i, j, grid) + diag(i, j, grid)


def P1(grid):
    if len(grid) == 0:
        return 0
    s = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j] == 'X'):
                s += test(i, j, grid)
    return s

def test2(i, j, grid):
    total = 0
    if i + 2 < len(grid) and j + 2 < len(grid[i]):
        cross = grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2]
        total += 1 if (grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] == "MAS") and (cross == "MAS" or cross[::-1] == "MAS") else 0
    if i + 2 < len(grid) and j - 2 >= 0:
        cross = grid[i+2][j] + grid[i+1][j-1] + grid[i][j-2]
        total += 1 if (grid[i][j] + grid[i+1][j-1] + grid[i+2][j-2] == "MAS") and (cross == "MAS" or cross[::-1] == "MAS") else 0
    if i - 2 >= 0 and j + 2 < len(grid[i]):
        cross = grid[i-2][j] + grid[i-1][j+1] + grid[i][j+2]
        total += 1 if (grid[i][j] + grid[i-1][j+1] + grid[i-2][j+2] == "MAS") and (cross == "MAS" or cross[::-1] == "MAS") else 0
    if i - 2 >= 0  and j - 2 >= 0:
        cross = grid[i-2][j] + grid[i-1][j-1] + grid[i][j-2]
        total += 1 if (grid[i][j] + grid[i-1][j-1] + grid[i-2][j-2] == "MAS") and (cross == "MAS" or cross[::-1] == "MAS") else 0
    return total
def P2(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'M':
                total += test2(i, j, grid)
    return total//2
def main():
    #i = sys.argv[1]
    i = "input.txt"
    f = open(i, 'r')
    s = f.readlines()
    s = [l.strip() for l in s]
    print(P2(s))


if __name__ == "__main__":
    main()

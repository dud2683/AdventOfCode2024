import sys
sys.setrecursionlimit(15000)

def P1(grid, orientation, pos, count):
    if count > 10000:
        return 1
    x, y = pos
    count+=1
    if grid[y][x] != 3:
        grid[y][x] = 2
    if orientation == 10:
        if y == 0:
            return 0
        if grid[y-1][x] == 1:
            return P1(grid, 11, pos, count)
        else:
            return P1(grid, orientation, (x, y -1), count)

    if orientation == 11:
        if x == len(grid[y])-1:
            return 0
        if grid[y][x+1] == 1:
            return P1(grid, 12, pos, count)
        else:
            return P1(grid, orientation, (x+1, y), count)

    if orientation == 12:
        if y == len(grid) -1:
            return 0
        if grid[y+1][x] == 1:
            return P1(grid, 13, pos, count)
        else:
            return P1(grid, orientation, (x, y+1), count)
    if orientation == 13:
        if x == 0:
            return 0
        if grid[y][x-1] == 1:
            return P1(grid, 10, pos, count)
        else:
            return P1(grid, orientation, (x-1, y), count)


def P2(grid, orientation, pos, locs, count):
    x, y = pos
    grid[y][x] = count
    locs[x][y].append(orientation)
    if orientation == 10:
        if y == 0:
            return
        if grid[y-1][x] == 1:
            P2(grid, 11, pos, locs, count)
            return
        else:
            P2(grid, orientation, (x, y -1), locs, count+1)
            return

    if orientation == 11:
        if x == len(grid[y])-1:
            return
        if grid[y][x+1] == 1:
            P2(grid, 12, pos, locs, count)
            return
        else:
            P2(grid, orientation, (x+1, y), locs, count+1)
            return

    if orientation == 12:
        if y == len(grid) -1:
            return
        if grid[y+1][x] == 1:
            P2(grid, 13, pos, locs, count)
            return
        else:
            P2(grid, orientation, (x, y+1), locs, count+1)
            return
    if orientation == 13:
        if x == 0:
            return
        if grid[y][x-1] == 1:
            P2(grid, 10, pos, locs, count)
            return
        else:
            P2(grid, orientation, (x-1, y), locs, count)
            return

def test(pos, ori, locs, grid):
    x, y = pos
    if x == 0 or y == 0:
        return False
    if y == len(grid)-1 or x == len(grid[0]) -1:
        return False
    if grid[y][x] == 2 and ori in locs[x][y]:
        return True
    
    if ori== 10:
        if y == 0:
            return False
        if grid[y-1][x] == 1:
            return test (pos, 11, locs, grid)
        else:
            return test((x, y -1),ori, locs, grid)

    if ori== 11:
        if x == len(grid[y])-1:
            return False
        if grid[y][x+1] == 1:
            return test(pos, 12, locs, grid)
        else:
            return test((x+1, y), ori, locs, grid)
            

    if ori== 12:
        if y == len(grid) -1:
            return False
        if grid[y+1][x] == 1:
            return test(pos, 13, locs ,grid)
        else:
            return test((x, y+1), ori, locs, grid)
    if ori== 13:
        if x == 0:
            return False
        if grid[y][x-1] == 1:
            return test(pos, 10, locs, grid)
        else:
            return test((x-1, y), ori, locs,grid)

def main():
    #i = sys.argv[1]
    i = "input.txt"
    f = open(i, 'r')
    s = f.readlines()
    grid = []
    look = {"^":10, ">":11, "v":12, "<":13}
    orientation = None
    pos = None
    for y, line in enumerate(s):
        l = []
        for x, char in enumerate(line):
            if char in look.keys():
                l.append(3)
                orientation = look[char]
                pos = x, y
            elif char == ".":
                l.append(0)
            elif char =="#":
                l.append(1)
        grid.append(l)
    P1(grid, orientation, pos,  2)
    t = 0
    for i, y in enumerate(grid) :
        for j,x in enumerate(y):
            if grid[i][j] == 2:
                grid[i][j] = 1
                t+=P1(grid, orientation, pos,  2)
                grid[i][j] = 2
    print(t)

if __name__ == "__main__":
    main()
 

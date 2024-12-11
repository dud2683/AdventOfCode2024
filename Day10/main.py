
def test2(g, i, j, num, path, spots):
	if g[i][j] != num:
		return
	path += f"[{i},{j}]"
	if num == 9:
		spots.add(path)
		return

	
	test2(g, i+1, j, num+1, path, spots)
	test2(g, i-1, j, num+1, path, spots)
	test2(g, i, j-1, num+1, path, spots)
	test2(g, i, j+1, num+1, path, spots)


def P2(grid):
	total = 0
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			spots = set()
			if grid[i][j] == 0:
				test2(grid, i, j, 0, "", spots)
				total += len(spots)
	return total


def test(g, i, j, num, spots):
	if g[i][j] != num:
		return
	if num == 9:
		spots.add(len(g)*i + j)
		return
	
	test(g, i+1, j, num+1, spots)
	test(g, i-1, j, num+1, spots)
	test(g, i, j-1, num+1, spots)
	test(g, i, j+1, num+1, spots)


def P1(grid):
	total = 0
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			spots = set()
			if grid[i][j] == 0:
				test(grid, i, j,0, spots)
				total += len(spots)
	return total
def main():
	#i = sys.argv[1]
	i = "input2.txt"
	f = open(i, 'r')
	s = f.readlines()
	grid = []
	for line in s:
		grid.append([10] + [int(x) for x in line.strip()] + [10])
	
	grid = [[10 for _ in range(len(grid[0]))]] + grid + [[10 for _ in range(len(grid[0]))]]
	print(P2(grid))


if __name__ == "__main__":
	main()


def getAll(grid, i, j, label, visited, replace):
	key = f"{i},{j}"
	if key in visited or grid[i][j] != label:
		return
	grid[i][j] = replace
	visited.add(key)
	getAll(grid, i, j+1, label, visited, replace)
	getAll(grid, i, j-1, label, visited, replace)
	getAll(grid, i-1, j, label, visited, replace)
	getAll(grid, i+1, j, label, visited, replace)
	
	

	

def transform(grid):
	labels = {}
	visited = set()
	for i, row in enumerate(grid):
		for j, c in enumerate(row):
			key = f"{i},{j}"
			if key in visited or c == 0:
				continue
			nl = labels.get(c, 0)
			labels[c] = nl +1
			nl = c + str(nl)
			getAll(grid, i, j, c, visited, nl)

def P2(grid):
	areas = {}
	perimiters = {}
	transform(grid)
	for i, row in enumerate(grid):
		for j, c in enumerate(row):
			if c == 0:
				continue
			areas[c] = areas.get(c,0) + 1
			# corners
			if grid[i][j+1] != c and grid[i-1][j] != c:
				perimiters[c] = perimiters.get(c,0) + 1
			
			if grid[i][j+1] != c and grid[i+1][j] != c:
				perimiters[c] = perimiters.get(c,0) + 1
			
			if grid[i][j-1] != c and grid[i-1][j] != c:
				perimiters[c] = perimiters.get(c,0) + 1

			if grid[i][j-1] != c and grid[i+1][j] != c:
				perimiters[c] = perimiters.get(c,0) + 1
			
			#inverted corners
			if grid[i][j+1] == c and grid[i-1][j] == c and grid[i-1][j+1] != c:
				perimiters[c] = perimiters.get(c,0) + 1
			
			if grid[i][j+1] == c and grid[i+1][j] == c and grid[i+1][j+1] != c:
				perimiters[c] = perimiters.get(c,0) + 1
			
			if grid[i][j-1] == c and grid[i-1][j] == c and grid[i-1][j-1] != c:
				perimiters[c] = perimiters.get(c,0) + 1

			if grid[i][j-1] == c and grid[i+1][j] == c and grid[i+1][j-1] != c:
				perimiters[c] = perimiters.get(c,0) + 1

			

	total = 0
	for k, v in areas.items():
		total += v * perimiters[k]
	return total

def P1(grid):
	areas = {}
	perimiters = {}
	transform(grid)
	for i, row in enumerate(grid):
		for j, c in enumerate(row):
			if c == 0:
				continue
			areas[c] = areas.get(c,0) + 1

			if grid[i][j+1] != c:
				perimiters[c] = perimiters.get(c,0) + 1
			
			if grid[i][j-1] != c:
				perimiters[c] = perimiters.get(c,0) + 1

			if grid[i+1][j] != c:
				perimiters[c] = perimiters.get(c,0) + 1

			if grid[i-1][j] != c:
				perimiters[c] = perimiters.get(c,0) + 1
	total = 0
	for k, v in areas.items():
		total += v * perimiters[k]
	return total
def main():
	#i = sys.argv[1]
	i = "input2.txt"
	f = open(i, 'r')

	s = f.readlines()
	grid = []

	for line in s:
		grid.append([0] + [x for x in line.strip()] + [0])
	
	grid = [[0 for _ in range(len(grid[0]))]] + grid + [[0 for _ in range(len(grid[0]))]]

	print(P2(grid))


if __name__ == "__main__":
	main()


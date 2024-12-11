def test(point, grid):
	x,y = len(grid[0]), len(grid)
	cx, cy = point
	ans = cx >x-1 or cy > y -1 or cx<0 or cy<0
	return not ans
def P1(grid):
	antenas = {}
	ans = []
	for i, row in enumerate(grid):
		for j, cell in enumerate(row):
			if cell == '.':
				continue
			if cell == '#':
				ans.append((i,j))
				continue
			if cell not in antenas.keys():
				antenas[cell] = []
			antenas[cell].append((i,j))
	
	size = max(len(grid), len(grid[0]))
	points = [[0 for _ in range(size) ] for _ in range(size)]
	total = 0
	ans2 = []
	for k, v in antenas.items():
		#print(k, v)
		for i in range(len(v)):
			for j in range(i + 1, len(v)):
				ax, ay = v[i]
				bx, by = v[j]
				deltax, deltay = (ax - bx), (ay -by)
				p1 = (ax + deltax, ay + deltay)
				p2 = (bx - deltax, by - deltay )
				a1 = 1 if test(p1, grid) and points[p1[0]][p1[1]] == 0 else 0
				if a1:
					points[p1[0]][p1[1]] = 1
					ans2.append(p1)
				a2 = 1 if test(p2, grid) and points[p2[0]][p2[1]] == 0 else 0
				if a2:
					points[p2[0]][p2[1]] = 1
					pass
					ans2.append(p2)
				total += a1
				total += a2
	return total	


	


def P2(grid):
	antenas = {}
	ans = []
	for i, row in enumerate(grid):
		for j, cell in enumerate(row):
			if cell == '.':
				continue
			if cell == '#':
				ans.append((i,j))
				continue
			if cell not in antenas.keys():
				antenas[cell] = []
			antenas[cell].append((i,j))
			ans.append((i,j))
	
	size = max(len(grid), len(grid[0]))
	points = [[0 for _ in range(size) ] for _ in range(size)]
	total = 0
	ans2 = []
	for k, v in antenas.items():
		#print(k, v)
		for i in range(len(v)):
			for j in range(i + 1, len(v)):
				ax, ay = v[i]
				bx, by = v[j]
				deltax, deltay = (ax - bx), (ay -by)
				p1 = (ax, ay)
				p2 = (ax, ay)
				a1, a2 = True, True
				while(test(p1, grid) or test(p2,grid)):
					a1 = 1 if test(p1, grid) and points[p1[0]][p1[1]] == 0 else 0
					a2 = 1 if test(p2, grid) and points[p2[0]][p2[1]] == 0 else 0
					if a1:
						points[p1[0]][p1[1]] = 1
						ans2.append(p1)
						total += a1
					p1 = p1[0] +deltax, p1[1] + deltay
					if a2:
						points[p2[0]][p2[1]] = 1
						ans2.append(p2)
						total += a2
					p2 = p2[0] - deltax, p2[1] - deltay
	
	ans2.sort()
	return len(set(ans2))
	ans.sort()
	print(ans2)
	print(ans)
	print(total, len(ans))
	return total	
def main():
	#i = sys.argv[1]
	i = "input.txt"
	f = open(i, 'r')
	grid = []
	s = f.readlines()
	for line in s:
		grid.append(line.strip())
	print(P2(grid))


if __name__ == "__main__":
	main()


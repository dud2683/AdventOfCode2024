
def P2(stone, b, memo):
	if b==75:
		return 1
	key = f"{b},"+stone 
	if key in memo.keys():
		return memo[key]
	if stone == "0":
		ans = P2(stone, b+1, memo)
		memo[key] = ans
		return ans
	elif len(stone)%2 == 0:
		ans = P2(stone[:len(stone)//2], b+1, memo) + P2(stone[len(stone)//2:], b+1, memo)
		return ans
	ans = P2(str(2024*int(stone)), b+1, memo)
	return ans

def P1(stones):
	for i in range(75):
		newstones = {}
		for stone, num in stones.items():
			s = (str(stone))
			if stone == 0:
				newstones[1] = newstones.get(1,0) + num
			elif len(s)%2 == 0:
				l = int(s[:len(s)//2])
				r = int(s[len(s)//2:])
				newstones[l] = newstones.get(l, 0) + num
				newstones[r] = newstones.get(r, 0) + num
			else:
				newstones[2024* stone] = newstones.get(2024* stone, 0) + num
		stones = newstones
	total = 0
	for k,v in stones.items():
		total += v

	return total

def main():
	#i = sys.argv[1]
	i = "input.txt"
	f = open(i, 'r')
	s = f.read().strip()
	nums = {int(x):1 for x in s.split()}
	print(nums)
	print(P1(nums))


if __name__ == "__main__":
	main()


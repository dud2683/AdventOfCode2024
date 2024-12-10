def P1(string):
	full = []
	b = True
	count=0
	nums = [int(c) for c in string]
	for n in nums:
		if b:
			full += [count for _ in range(n)]
			count+=1
			b = False
		else:
			full += ['.' for _ in range(n)]
			b = True
	l = 0
	r = len(full) -1
	try:
		while l < r:
			while full[l] != '.':
				l+=1
			while full[r] == '.':
				r-=1
			if not l<r:
				break
			temp = full[l]
			full[l] = full[r]
			full[r] = temp
	except IndexError:
		pass
	s = 0
	for i, n in enumerate(full):
		if n == '.':
			return s
		s+=i*n
	return s

def P2(string):
	full = []
	b = True
	count=0
	nums = [int(c) for c in string]
	for n in nums:
		if b:
			full += [count for _ in range(n)]
			count+=1
			b = False
		else:
			full += ['.' for _ in range(n)]
			b = True
	
	
	r = len(full)-1
	completed_ids = set()
	while r>0:
		while full[r] == '.':
			r-=1

		id = full[r]
		if id in completed_ids:
			r-=1
			continue

		completed_ids.add(id)
		s = 0
		while full[r] == id: 
			r-=1
			s+=1
		p = 0
		while p < r:
			while full[p] != '.' and p <= r:
				p+=1
			q = 0
			while full[p] == '.' and q < s and p <= r:
				p+=1
				q+=1
			if q == s:
				for i in range(0, q):
					full[p-s +i] = id
					full[r+1+i] = '.'
				break


	s = 0
	print(full)
	for i, n in enumerate(full):
		if n == '.':
			continue
		s+=i*n
	return s
	
def main():
	#i = sys.argv[1]
	i = "input2.txt"
	f = open(i, 'r')
	s = (f.read()).strip()
	print(P2(s))


if __name__ == "__main__":
	main()


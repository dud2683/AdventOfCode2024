import sys

def P1(i, o):
    f = open(i, 'r')
    left = []
    right = []
    for line in f.readlines():
        nums = line.split(" ")
        left.append(int(nums[0]))
        right.append(int(nums[-1]))
    
    f.close()
    left.sort()
    right.sort()
    s = 0
    for l, r in zip(left, right):
        s += abs(l - r)
    print(s)
    f = open(o, 'w')
    f.write(str(s))
    f.close()
    exit(0)

def P2(i, o):
    f = open(i, 'r')
    left = {}
    right = {}
    for line in f.readlines():
        nums = line.split(" ")
        l = int(nums[0])
        r = int(nums[-1])

        if l not in left.keys():
            left[l] = 0
        if r not in right.keys():
            right[r] = 0

        left[l] +=1
        right[r] +=1
    s = 0
    for k, v in left.items():
        r = right.get(k,0)
        s+= r*v*k
    print(s)



def main():
    if len(sys.argv) == 3:
        in_file = sys.argv[1]
        out_file = sys.argv[2]
    else:
        in_file = "input.txt" 
        out_file = "out.txt" 

    P2(in_file, out_file)

if __name__ == "__main__":
    main()

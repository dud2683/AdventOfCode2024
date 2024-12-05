def P1(constraints, orders):
    total = 0
    for order in orders:
        indexs = {}
        for i, num in enumerate(order):
            indexs[num] = i
        valid = True
        for constraint in constraints:
            a,b = constraint
            if a not in indexs.keys() or b not in indexs.keys():
                continue
            if indexs[a] > indexs[b]:
                valid = False
                break
        if valid:
            total += order[len(order)//2]

    return total

def fix(indexs, constraints):
    a,b = verify(constraints,indexs) 
    while a != -1:
        temp = indexs[a]
        indexs[a] = indexs[b]
        indexs[b] = temp
        a,b = verify(constraints, indexs)

    for k, v in indexs.items():
        if v == len(indexs.items())//2:
            return k

        pass



def verify(constraints, indexs):
    for constraint in constraints:
        a,b = constraint
        if a not in indexs.keys() or b not in indexs.keys():
            continue
        if indexs[a] > indexs[b]:
            return a, b
    return -1, -1

def P2(constraints, orders):
    total = 0
    for order in orders:
        indexs = {}
        for i, num in enumerate(order):
            indexs[num] = i
        valid = True
        for constraint in constraints:
            a,b = constraint
            if a not in indexs.keys() or b not in indexs.keys():
                continue
            if indexs[a] > indexs[b]:
                valid = False
                break
        if not valid:
            total += fix(indexs, constraints)

    return total

def main():
    #i = sys.argv[1]
    i = "input.txt"
    f = open(i, 'r')
    s = f.read()
    parts = s.split("\n\n")
    constraints = []
    for line in parts[0].split('\n'):
        nums = line.split('|')
        constraints.append((int(nums[0]), int(nums[1])))

    orders = []
    for line in parts[1].split('\n')[:-1]:
        orders.append( [int(x) for x in line.split(',')])


    print(P2(constraints, orders))


if __name__ == "__main__":
    main()
 

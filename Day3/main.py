import sys
import re

def P1(s):
    muls = re.findall(r"mul\([0-9]+,[0-9]+\)", s)
    sums = 0
    for mul in muls:
        l = mul.find('(')
        c = mul.find(',')
        r = mul.find(')')
        left = int(mul[l+1:c])
        right= int(mul[c+1:r])
        sums+=left*right
    return sums

def P2(s):
    valid = [0 for _ in range(len(s))]
    for match in re.finditer(r"do\(\)", s):
        valid[match.span()[0]] = 1
    for match in re.finditer(r"don't\(\)", s):
        valid[match.span()[0]] = -1

    cur = 1
    for i in range(len(s)):
        if valid[i] == 1:
            cur = 1
        elif valid[i] == -1:
            cur = -1
        else:
            valid[i] = cur


    muls = re.finditer(r"mul\([0-9]+,[0-9]+\)", s)
    sums = 0
    

    for mul in muls:
        if valid[mul.span()[0]] == -1:
            continue
        mul = mul.group()
        l = mul.find('(')
        c = mul.find(',')
        r = mul.find(')')
        left = int(mul[l+1:c])
        right= int(mul[c+1:r])
        sums+=left*right
    return sums

def main():
    input_file = sys.argv[1]
    f = open(input_file)
    string = f.read()
    print(P2(string))

if __name__ == "__main__":
    main()

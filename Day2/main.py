import sys

def P1(i,o):
    f = open(i,'r')
    safe = 0
    for line in f.readlines():
        nums = [int(x) for x in line.split(" ")]
        if nums[0] == nums[1]:
            continue
        cur = nums[0]
        isDec = nums[1] < nums[0]
        isSafe = True
        for num in nums[1:]:
            if isDec:
                diff = cur - num 
                if diff > 3 or diff < 1:
                    isSafe = False
                    break
                cur = num
            else:
                diff = num - cur
                if diff > 3 or diff < 1:
                    isSafe = False
                    break
                cur = num
        if isSafe:
            safe+=1
    print(safe)

def test(nums, damp=False):
     orig = damp
     if len(nums) < 2:
         return 1
     if nums[0] == nums[1]:
         if damp:
             return 0
         else:
             return 1 if test(nums[1:], True)==1 or test([nums[0]] + nums[2:], True) else 0
     cur = nums[0]
     isDec = nums[1] < nums[0]
     for num in nums[1:]:
         if isDec:
             diff = cur - num 
             if diff > 3 or diff < 1:
                 if damp and not orig: 
                     return 1 if test(nums[1:], True)==1 or test([nums[0]] + nums[2:], True) ==1  else 0
                 if damp:
                     return 0
                 else:
                     damp = True
                     continue
             cur = num
         else:
             diff = num - cur
             if diff > 3 or diff < 1:
                 if damp and not orig: 
                     return 1 if test(nums[1:], True)==1 or test([nums[0]] + nums[2:], True) == 1 else 0
                 if damp:
                     return 0
                 else:
                     damp = True
                     continue
             cur = num
     return 1
def P2(i,o):
    f = open(i,'r')
    safe = 0
    for line in f.readlines():
        nums = [int(x) for x in line.split(" ")]
        safe += test(nums)
    print(safe)


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

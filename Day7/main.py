def test(target, nums, cur):
    if len(nums) == 0:
        return target == cur
    return test(target, nums[1:], cur + nums[0]) or test(target, nums[1:], cur*nums[0])
def P1(res, nums):
    if test(res, nums, 0):
        return res
    else:
        return 0
def test2(target, nums, cur):
    if len(nums) == 0:
        return target == cur
    return test2(target, nums[1:], cur + nums[0]) or test2(target, nums[1:], cur*nums[0]) or \
            test2(target, nums[1:], int(str(cur) + str(nums[0])))
def P2(res, nums):
    return res if test2(res, nums, 0) else 0

def main():
    #i = sys.argv[1]
    i = "input.txt"
    f = open(i, 'r')
    total = 0
    s = f.readlines()
    for line in s:
        parts = line.split(": ")
        res = int(parts[0])
        nums = [int(x) for x in parts[1].split(" ")]
        total += P2(res, nums)
    print(total)


if __name__ == "__main__":
    main()
 

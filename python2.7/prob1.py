

nums = {}
index = 1

for num in map(int, raw_input().split()):
    if num not in nums:
        nums[num] = index
        index += 1
    else:
        print "{} is a duplicate".format(num)

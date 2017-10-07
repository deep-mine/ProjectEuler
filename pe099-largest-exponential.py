import math

with open("p099_base_exp.txt") as b:
    be = b.read().split("\n")

max_num = -1
ind = 0
found = -1
nums = []
for i in be:
    nums.append(i.split(","))



for i in range(len(nums)):
    ind += 1
    val = math.log(int(nums[i][0]),10)*int(nums[i][1])
    if val > max_num:
        max_num = val
        found = ind
print(max_num,found)

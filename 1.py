nums = open("input1.txt", "r")
nums = nums.read().split("\n")
nums = [int(n) for n in nums]


ans1 = 0

for i in range(len(nums) - 1):
    if (nums[i+1] > nums[i]):
        ans1 += 1

print(ans1)


ans2 = 0

for i in range(len(nums) - 3):
    if (nums[i+3] > nums[i]):
        ans2 += 1

print(ans2)
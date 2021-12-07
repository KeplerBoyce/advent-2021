lines = open("input7.txt", "r")
lines = lines.read().split("\n")
if lines[-1] == "":
	lines.pop()
    
nums = lines[0].split(",")
nums = [int(num) for num in nums]

guess = 0
bestguess = 0
total = 0
besttotal = -1

while guess <= max(nums):
    total = 0
    for num in nums:
        temp = abs(num - guess)
        total += (temp + 1) * temp/2
    if besttotal == -1:
        besttotal = total
    if total < besttotal:
        besttotal = total
        bestguess = guess
    guess += 1

print(besttotal)
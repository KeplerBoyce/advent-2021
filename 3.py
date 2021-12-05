lines = open("input3.txt", "r")
lines = lines.read().split("\n")
if lines[-1] == "":
	lines.pop()

gamma = 0
epsilon = 0

for i in range(len(lines[0])):
    num0 = 0
    num1 = 0
    for line in lines:
        if line[len(line) - (i+1)] == "0":
            num0 += 1
        else:
            num1 += 1
    if num1 > num0:
        gamma += 2**i
    else:
        epsilon += 2**i

print(gamma*epsilon)


oxygen = 0
co2 = 0
templines1 = lines.copy()
templines2 = lines.copy()

for i in range(len(lines[0])):
    selector1 = "0"
    selector2 = "1"
    
    num0 = 0
    num1 = 0
    for line in templines1:
        if line[i] == "0":
            num0 += 1
        else:
            num1 += 1
    if num1 >= num0:
        selector1 = "1"
        
    num0 = 0
    num1 = 0
    for line in templines2:
        if line[i] == "0":
            num0 += 1
        else:
            num1 += 1
    if num1 >= num0:
        selector2 = "0"
    
    j = 0
    while j < len(templines1):
        if len(templines1) == 1:
            oxygen = int(templines1[0], 2)
        if templines1[j][i] != selector1:
            templines1.pop(j)
        else:
            j += 1
          
    j = 0
    while j < len(templines2):
        if len(templines2) == 1:
            co2 = int(templines2[0], 2)
        if templines2[j][i] != selector2:
            templines2.pop(j)
        else:
            j += 1

print(oxygen*co2)
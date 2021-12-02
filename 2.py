lines = open("input2.txt", "r")
lines = lines.read().split("\n")

depth = 0
forward = 0

for i in lines:
    temp = i.split(" ")
    if temp[0] == "forward":
        forward += int(temp[1])
    elif temp[0] == "up":
        depth -= int(temp[1])
    else:
        depth += int(temp[1])
        
print(depth*forward)


depth = 0
forward = 0
aim = 0

for i in lines:
    temp = i.split(" ")
    if temp[0] == "forward":
        forward += int(temp[1])
        depth += aim*int(temp[1])
    elif temp[0] == "up":
        aim -= int(temp[1])
    else:
        aim += int(temp[1])
        
print(depth*forward)
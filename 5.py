lines = open("input5.txt", "r")
lines = lines.read().split("\n")
if lines[-1] == "":
	lines.pop()

vents = []
for line in lines:
    temp = line.split(" -> ")
    temp2 = temp[0].split(",")
    temp3 = temp[1].split(",")
    vents.append([int(temp2[0]), int(temp2[1]), int(temp3[0]), int(temp3[1])])

grid = []
for i in range(1000):
    g = []
    for j in range(1000):
        g.append(0)
    grid.append(g)

for vent in vents:
    if vent[0] == vent[2]:
        if vent[1] > vent[3]:
            for i in range(vent[3], vent[1]+1):
                grid[vent[0]][i] += 1
        else:
            for i in range(vent[1], vent[3]+1):
                grid[vent[0]][i] += 1
    elif vent[1] == vent[3]:
        if vent[0] > vent[2]:
            for i in range(vent[2], vent[0]+1):
                grid[i][vent[1]] += 1
        else:
            for i in range(vent[0], vent[2]+1):
                grid[i][vent[1]] += 1
    else:
        if vent[0] > vent[2]:
            if vent[1] > vent[3]:
                for i in range(vent[0] - vent[2] + 1):
                    grid[vent[0]-i][vent[1]-i] += 1
            else:
                for i in range(vent[0] - vent[2] + 1):
                    grid[vent[0]-i][vent[1]+i] += 1
        else:
            if vent[1] > vent[3]:
                for i in range(vent[2] - vent[0] + 1):
                    grid[vent[0]+i][vent[1]-i] += 1
            else:
                for i in range(vent[2] - vent[0] + 1):
                    grid[vent[0]+i][vent[1]+i] += 1

count = 0

for i in range(1000):
    for j in range(1000):
        if grid[i][j] > 1:
            count += 1

print(count)
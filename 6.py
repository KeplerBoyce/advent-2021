lines = open("input6.txt", "r")
lines = lines.read().split("\n")
if lines[-1] == "":
	lines.pop()

fish = lines[0].split(",")
fish = [int(f) for f in fish]

numeach = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for f in fish:
    for i in range(9):
        if f == i:
            numeach[i] += 1

for day in range(256):
    temp = numeach[0]
    numeach[0] = numeach[1]
    numeach[1] = numeach[2]
    numeach[2] = numeach[3]
    numeach[3] = numeach[4]
    numeach[4] = numeach[5]
    numeach[5] = numeach[6]
    numeach[6] = numeach[7] + temp
    numeach[7] = numeach[8]
    numeach[8] = temp

total = 0

for i in range(9):
    total += numeach[i]

print(total)
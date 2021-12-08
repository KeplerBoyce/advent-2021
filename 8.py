lines = open("input8.txt", "r")
lines = lines.read().split("\n")
if lines[-1] == "":
	lines.pop()

patterns = []
outputs = []
for i in range(len(lines)):
    a = lines[i].split(" ")
    patterns.append(a[0:10])
    outputs.append(a[11:15])

num = 0
for out in outputs:
    for digit in out:
        if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
            num += 1

print(num)


def split(s):
    return [c for c in s]

total = 0
for i in range(len(lines)):
    pat = patterns[i]
    out = outputs[i]
    codes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    right = []
    topright = ""
    infive = []
    intwo = []
    infour = []
    center = ""
    for digit in pat:
        if len(digit) == 2:
            right = split(digit)
    for digit in pat:
        if len(digit) == 6:
            for letter in right:
                if letter not in split(digit):
                    topright = letter
    for digit in pat:
        if len(digit) == 4:
            infour = split(digit)
        if len(digit) == 5:
            b = True
            for letter in right:
                if letter not in split(digit):
                    b = False
            if not b:
                if topright in split(digit):
                    intwo = split(digit)
                else:
                    infive = split(digit)
    for char in ["a", "b", "c", "d", "e", "f", "g"]:
        if char in intwo and char in infour and char in infive:
            center = char
    for digit in pat:
        if len(digit) == 2:
            codes[1] = "".join(sorted(split(digit)))
        elif len(digit) == 3:
            codes[7] = "".join(sorted(split(digit)))
        elif len(digit) == 4:
            codes[4] = "".join(sorted(split(digit)))
        elif len(digit) == 5:
            b = True
            for letter in right:
                if letter not in split(digit):
                    b = False
            if b:
                codes[3] = "".join(sorted(split(digit)))
            else:
                if topright in split(digit):
                    codes[2] = "".join(sorted(split(digit)))
                else:
                    codes[5] = "".join(sorted(split(digit)))
        elif len(digit) == 6:
            if center in split(digit):
                b = True
                for letter in right:
                    if letter not in split(digit):
                        b = False
                if b:
                    codes[9] = "".join(sorted(split(digit)))
                else:
                    codes[6] = "".join(sorted(split(digit)))
            else:
                codes[0] = "".join(sorted(split(digit)))
        elif len(digit) == 7:
            codes[8] = "".join(sorted(split(digit)))
    number = ""
    for digit in out:
        number += str(codes.index("".join(sorted(split(digit)))))
    total += int(number)

print(total)
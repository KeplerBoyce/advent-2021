lines = open("input4.txt", "r")
lines = lines.read().split("\n")

nums = lines[0].split(",")
nums = [int(num) for num in nums]

boards = []
for i in range(2, len(lines)):
    if lines[i] == "":
        boards.append([lines[i-5], lines[i-4], lines[i-3], lines[i-2], lines[i-1]])
for board in boards:
    for i in range(5):
        temp = board[i].split(" ")
        j = 0
        while j < len(temp):
            if temp[j] == "":
                temp.pop(j)
            else:
                j += 1
        board[i] = [int(i) for i in temp]

winsum = 0
prevnum = 0
finalnum = 0
found = False
for num in nums:
    for board in boards:
        for i in range(5):
            if not found and (board[i] == [-1, -1, -1, -1, -1] or [board[0][i], board[1][i], board[2][i], board[3][i], board[4][i]] == [-1, -1, -1, -1, -1]):
                found = True
                finalnum = prevnum
                for j in range(5):
                    for k in range(5):
                        if board[j][k] != -1:
                            winsum += board[j][k]
            elif not found:
                for j in range(5):
                    if board[i][j] == num:
                        board[i][j] = -1
    prevnum = num

print(winsum*finalnum)

solved = []
ones = []
for i in range(len(boards)):
    solved.append(0)
    ones.append(1)
found = False
winsum = 0
prevnum = 0
finalnum = 0
for num in nums:
    for boardnum in range(len(boards)):
        board = boards[boardnum]
        for i in range(5):
            if not found and (board[i] == [-1, -1, -1, -1, -1] or [board[0][i], board[1][i], board[2][i], board[3][i], board[4][i]] == [-1, -1, -1, -1, -1]):
                solved[boardnum] = 1
                if solved == ones:
                    found = True
                    finalnum = prevnum
                    for j in range(5):
                        for k in range(5):
                            if board[j][k] != -1:
                                winsum += board[j][k]
            elif not found:
                for j in range(5):
                    if board[i][j] == num:
                        board[i][j] = -1
    prevnum = num

print(winsum*finalnum)
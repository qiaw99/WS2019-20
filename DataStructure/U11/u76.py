# nxn chessboard
n = 10
# number of dragons on the chessboard
dragons = 10

solution = [-1]*n
captured = [[0 for i in range(n)] for i in range(n)]
number = 0
local_calls = 0
total_calls = 0

def init():
	global captured

def isCaptured(x, y):
    global captured
    return captured[x][y]

def capture(x, y):
    for i in range(n):
        captured[i][y] += 1
        captured[x][i] += 1

    # this point double counted in prev. for-loop,
    captured[x][y] -= 1

    i = x + 1
    j = y + 1
    while (i < n and j < n):
        captured[i][j] += 1
        i += 1
        j += 1

    i = x + 1
    j = y - 1
    while (i < n and j >= 0):
        captured[i][j] += 1
        i += 1
        j -= 1


    i = x - 1
    j = y - 1
    while (i >= 0 and j >= 0):
        captured[i][j] += 1
        i -= 1
        j -= 1

    i = x - 1
    j = y + 1
    while (i >= 0 and j < n):
        captured[i][j] += 1
        i -= 1
        j += 1

    if x - 2 >= 0:
        if y - 1 >= 0:
            captured[x-2][y-1] += 1
        if y + 1 < n:
            captured[x-2][y+1] += 1

    if x + 2 < n:
        if y - 1 >= 0:
            captured[x + 2][y - 1] += 1
        if y + 1 < n:
            captured[x + 2][y + 1] += 1

    if y - 2 >= 0:
        if x - 1 >= 0:
            captured[x - 1][y - 2] += 1
        if x + 1 < n:
            captured[x + 1][y - 2] += 1

    if y + 2 < n:
        if x - 1 >= 0:
            captured[x - 1][y + 2] += 1
        if x + 1 < n:
            captured[x + 1][y + 2] += 1

def free (x, y):
    for i in range(n):
        captured[i][y] -= 1
        captured[x][i] -= 1

    # this point double counted in prev. for-loop,
    captured[x][y] += 1

    i = x + 1
    j = y + 1
    while (i < n and j < n):
        captured[i][j] -= 1
        i += 1
        j += 1

    i = x + 1
    j = y - 1
    while (i < n and j >= 0):
        captured[i][j] -= 1
        i += 1
        j -= 1

    i = x - 1
    j = y - 1
    while (i >= 0 and j >= 0):
        captured[i][j] -= 1
        i -= 1
        j -= 1

    i = x - 1
    j = y + 1
    while (i >= 0 and j < n):
        captured[i][j] -= 1
        i -= 1
        j += 1

    if x - 2 >= 0:
        if y - 1 >= 0:
            captured[x-2][y-1] -= 1
        if y + 1 < n:
            captured[x-2][y+1] -= 1
    if x + 2 < n:
        if y - 1 >= 0:
            captured[x + 2][y - 1] -= 1
        if y + 1 < n:
            captured[x + 2][y + 1] -= 1

    if y - 2 >= 0:
        if x - 1 >= 0:
            captured[x - 1][y - 2] -= 1
        if x + 1 < n:
            captured[x + 1][y - 2] -= 1

    if y + 2 < n:
        if x - 1 >= 0:
            captured[x - 1][y + 2] -= 1
        if x + 1 < n:
            captured[x + 1][y + 2] -= 1


def find(x, d):
    global captured, solution, number, total_calls, local_calls, dragons
    total_calls += 1
    local_calls += 1
    if x == d:
        number += 1
        print("Soluiton: ", number, " Coord: ", solution)
        print("Number of local calls ", local_calls)
        local_calls = 0
        return
    for j in range(n):
        if not isCaptured(x, j):
            solution[x] = j
            capture(x, j)
            find(x + 1, dragons)
            free(x, j)


print("")
print("Coordinate '-1' means no Dragon in that line")
print("")
find(0, dragons)
print("")
print("Number of total calls ", total_calls)



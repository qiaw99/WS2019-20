n = 8
solution = [0]*n
captured = [[0 for i in range(n)] for i in range(n)]
number = 0
calls = 0

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
    while (i >= n and j < n):
        captured[i][j] += 1
        i -= 1
        j += 1
        
        
def free (x, y):
   #print("clearing ", x, " ", y)
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

             

def find(x):
    global captured, solution, number, calls
    if x == n:
        number += 1
        print (number, solution)
        return
    for j in range(n):
        if not isCaptured(x, j):
            solution[x] = j
            capture(x, j)
            find(x + 1)
            free(x, j)
        
           
find(0)

    
    
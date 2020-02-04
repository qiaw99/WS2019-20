def indexOf(ls, x):
    for i in range(len(ls)):
        if ls[i] == x:
            return i
    return -1

s = "abcdbc"
t = "abcabc"
k = 2
dp = [[0 for _ in range(len(t))] for _ in range(len(s))]
for i in range(len(s)):
    for j in range(len(t)):
        if(s[i] == t[j]):
            if(i == 0):
                dp[0][j] = 1
            elif(j == 0):
                dp[i][0] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = 0
res = []
counter = 0
print(dp)
for i in dp:
    if indexOf(i, k) != -1:
        print(counter, indexOf(i, k))
    counter += 1

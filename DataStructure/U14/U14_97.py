money = 143
coins = [1, 2, 5, 10, 20, 50]
res = []
memo = [[None] for _ in range(money + 1)]
memo[1] = [1]
memo[2] = [2]
memo[5] = [5]
memo[10] = [10]
memo[20] = [20]
counter = 0

def changeMoney(x):
    global coins, res, memo, counter
    if(memo[x] != [None]):
        res.extend(memo[x])
        return 
    for temp in reversed(coins):
        if temp <= x:
            res.append(temp)
            counter += 1
            return changeMoney(x-temp)

changeMoney(money)
print(res)
print(counter)

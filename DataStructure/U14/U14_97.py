nums = 34
coins= [1,2,5,10]
temp = nums
dp = [float("inf") for _ in range(nums)]
dp[0] = 0
for i in range(1,nums):
    for j in range(len(coins)):
        if(coins[j] <= nums):
            dp[i] = min(dp[i], dp[i-coins[j]]+1)
print(dp)            
print(dp[nums-1])

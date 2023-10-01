n = int(input().strip())
dp = [1000000 for _ in range(n*4)]
dp[n] = 0
for i in range(n-1, 0, -1):
    dp[i] = min(dp[i], dp[i+1]+1, dp[i*3]+1, dp[i*2]+1)

print(dp[1])

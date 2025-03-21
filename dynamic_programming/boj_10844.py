import sys

input = sys.stdin.readline

n = int(input())
dp = [[0]*10 for _ in range(n+1)]
dp[1] = [0,1,1,1,1,1,1,1,1,1]

for i in range(2, n+1):
    dp[i][0] = dp[i-1][1]
    dp[i][1] = dp[i-1][0] + dp[i-1][2]
    dp[i][2] = dp[i-1][1] + dp[i-1][3]
    dp[i][3] = dp[i-1][2] + dp[i-1][4]
    dp[i][4] = dp[i-1][3] + dp[i-1][5]
    dp[i][5] = dp[i-1][4] + dp[i-1][6]
    dp[i][6] = dp[i-1][5] + dp[i-1][7]
    dp[i][7] = dp[i-1][6] + dp[i-1][8]
    dp[i][8] = dp[i-1][7] + dp[i-1][9]
    dp[i][9] = dp[i-1][8]

answer = sum(dp[n])
print(answer%1000000000)
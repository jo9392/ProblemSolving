import sys

input = sys.stdin.readline
n = int(input())
stair_list = list()
for i in range(n):
    stair_list.append(int(input().strip()))

dp = list(0 for _ in range(n))
dp[0] = stair_list[0]
if n > 1:
    dp[1] = stair_list[0]+stair_list[1]
if n > 2:
    dp[2] = max(stair_list[0], stair_list[1])+stair_list[2]

if n > 3:
    for i in range(3, n):
        if dp[i-3]+stair_list[i-1] < dp[i-2]:
            dp[i] = dp[i-2]+stair_list[i]   # 1 0 1인 상황
        else:
            dp[i] = dp[i-3]+stair_list[i-1]+stair_list[i]   # 0 1 1인 상황
print(dp[n-1])
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
coins = list()
for i in range(n):
    coins.append(int(input()))

dp = list(0 for _ in range(k+1))
for c in coins:
    if c <= k:
        dp[c] += 1
    for i in range(k+1):
        if i-c >= 1:
            dp[i] += dp[i-c]
print(dp[k])
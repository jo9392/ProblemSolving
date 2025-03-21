import sys

input = sys.stdin.readline

t = int(input())
dp = [[0]*15 for _ in range(15)]
dp[0] = [i for i in range(15)]
for k in range(1,15):
    for n in range(1,15):
        dp[k][n] = sum(dp[k-1][:n+1])
# print(dp)
for _ in range(t):
    floor = int(input())
    door = int(input())
    print(dp[floor][door])
    
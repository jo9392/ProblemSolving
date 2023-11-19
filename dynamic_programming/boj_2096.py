import sys

input = sys.stdin.readline
n = int(input())
input_list = []
max_dp = [[0]*3 for _ in range(2)]
min_dp = [[0]*3 for _ in range(2)]
for i in range(n):
    a, b, c = list(map(int, input().split()))
    max_dp[1][0] = max(max_dp[0][0], max_dp[0][1]) + a
    max_dp[1][1] = max(max_dp[0][0], max_dp[0][1], max_dp[0][2]) + b
    max_dp[1][2] = max(max_dp[0][1], max_dp[0][2]) + c

    min_dp[1][0] = min(min_dp[0][0], min_dp[0][1]) + a
    min_dp[1][1] = min(min_dp[0][0], min_dp[0][1], min_dp[0][2]) + b
    min_dp[1][2] = min(min_dp[0][1], min_dp[0][2]) + c

    for p in range(3):
        max_dp[0][p] = max_dp[1][p]
        min_dp[0][p] = min_dp[1][p]

print(max(max_dp[1]), min(min_dp[1]))
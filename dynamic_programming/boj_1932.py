import sys
input = sys.stdin.readline

n = int(input())
table_list = list()
dp = list()
for i in range(n):
    table_list.append(list(map(int, input().split())))

for i in range(n):
    dp.append([0]*(i+1))

for i in range(n):
    for j in range(i+1):
        if j != 0 and j != i and i != 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + table_list[i][j]
        elif i == 0 and j == 0:
            dp[i][j] = table_list[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j] + table_list[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + table_list[i][j]

print(max(dp[n-1]))
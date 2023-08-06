import sys
input=sys.stdin.readline

n, m = list(map(int, input().split()))
table_list = list()
pos_list = list()
for i in range(n):
    table_list.append(list(map(int, input().split())))

for i in range(m):
    pos_list.append(list(map(int, input().split())))

dp = [[0]*n for i in range(n)]
dp[0][0] = table_list[0][0]
for i in range(1,n):
    dp[0][i] = table_list[0][i]+dp[0][i-1]
    dp[i][0] = table_list[i][0]+dp[i-1][0]

for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = table_list[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for x1, y1, x2, y2 in pos_list:
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    if x1 > 0 and y1 > 0:
        print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])
    elif x1 > 0:
        print(dp[x2][y2] - dp[x1 - 1][y2])
    elif y1 > 0:
        print(dp[x2][y2] - dp[x2][y1-1])
    else:
        print(dp[x2][y2])

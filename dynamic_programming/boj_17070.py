# 가로 : (0,1), 세로 : (1,0), 대각선 : (1,1)
# 각 칸마다 도달하는 경우의 수를 dp에 저장, 더해가면서 n,n에 도달하는 것
# dp의 기준은 오른쪽 끝 파이프가 도달한 좌표
# 각 칸으로 이동할 때 따져야 할 조건은 파이프의 상태, 현재 좌표, 벽의 유무
# 0 가로, 1 세로, 2 대각선

import sys
input = sys.stdin.readline

n = int(input())
house_graph = list()
house_graph.append([0]*(n+1))
for i in range(n):
    temp_list = [0]+list(map(int, input().split()))
    house_graph.append(temp_list)

dp = [[[0]*(3) for _ in range(n+1)] for _ in range(n+1)]
dp[1][2][0] = 1

for i in range(1,n+1):
    for j in range(3,n+1):
        if house_graph[i][j] == 1 or house_graph[i-1][j] == house_graph[i][j-1] == 1: #아예 진입이 불가할 경우
            dp[i][j] = [0,0,0]
        elif house_graph[i-1][j] == 1: # 가로 이동만 가능할 경우
            dp[i][j] = [dp[i][j-1][0]+dp[i][j-1][2], 0, 0]
        elif house_graph[i][j-1] == 1: # 세로 이동만 가능한 경우
            dp[i][j] = [0, dp[i-1][j][1]+dp[i-1][j][2], 0]
        elif house_graph[i-1][j-1] == 1: # 가로, 세로 이동만 가능한 경우
            dp[i][j] = [dp[i][j-1][0], dp[i - 1][j][1], 0]
        elif house_graph[i][j-1] == house_graph[i-1][j] == house_graph[i-1][j-1] == 0: #모두 이동할 수 있는 경우
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
            dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

print(sum(dp[n][n]))
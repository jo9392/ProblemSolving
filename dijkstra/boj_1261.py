import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
maze = []
# padding = 1
for i in range(M):
    maze.append(list(map(int, input()[:-1])) + [0])
maze.append([0]*(N+1))

def dijkstra():
    dp = []
    for i in range(M+1):
        dp.append([])
        for j in range(N+1):
            dp[i].append(i+j+1)   #초기 dp 할당값은 i+j+1
    dp[0][0] = 0
    hq = []
    heapq.heappush(hq, [0,[0,0]])   #부순 벽, 현재 위치

    pos_move = [[0,1],[1,0],[0,-1],[-1,0]]
    while(hq):
        crash, [temp_pos_x, temp_pos_y] = heapq.heappop(hq)
        if temp_pos_x == N-1 and temp_pos_y == M-1:
            break
        if crash > dp[temp_pos_x][temp_pos_y]:     #최소 조건 만족하지 못할 시 pop
            continue

        #상하좌우 이동, 이동할 값이 0이면 현재 값, 1이면 현재 값+1로 비교 및 할당
        for [x, y] in pos_move:
            next_pos_x = temp_pos_x + x
            next_pos_y = temp_pos_y + y
            if 0 <= next_pos_x <= M-1 and 0 <= next_pos_y <= N-1 and crash + maze[next_pos_x][next_pos_y] < dp[next_pos_x][next_pos_y]:
                next_crash = crash + maze[next_pos_x][next_pos_y]
                heapq.heappush(hq, [next_crash, [next_pos_x, next_pos_y]])
                dp[next_pos_x][next_pos_y] = next_crash
    return dp

dp = dijkstra()
print(dp[M-1][N-1])
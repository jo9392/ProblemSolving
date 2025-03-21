import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
visited_dfs = [0]*(n+1)
visited_bfs = [0]*(n+1)

def dfs(v):
    visited_dfs[v] = 1
    dfs_answer = str(v) + " "
    for i in range(1, n+1):
        if graph[v][i] == 1 and visited_dfs[i] == 0:
            dfs_answer += dfs(i)
    return dfs_answer


def bfs(v):
    bfs_answer = ""
    visited_bfs[v] = 1
    dq = deque()
    dq.append(v)
    while(dq):
        temp = dq.popleft()
        bfs_answer += str(temp) + " "
        for i in range(1, n+1):
            if graph[temp][i] == 1 and visited_bfs[i] == 0:
                dq.append(i)
                visited_bfs[i] = 1
    return bfs_answer

dfs_answer = dfs(v)
bfs_answer = bfs(v)

print(dfs_answer)
print(bfs_answer)

# 1번부터 검사, 연결되어있는 곳으로 넘어가기
global visited
def bfs(start_node, visited, computers):
    for i in range(len(visited)):
        if computers[start_node][i] == 1 and start_node != i and visited[i] == 0:
            visited[i] = 1
            bfs(i, visited, computers)
    

def solution(n, computers):
    visited = [0]*n
    answer = 0
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            answer += 1
            bfs(i, visited, computers)
    
    return answer
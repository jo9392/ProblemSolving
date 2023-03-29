from collections import deque
def solution(k, dungeons):
    dq = deque()
    visited = [False for i in range(len(dungeons))]
    cnt = 0
    dq.append([k, visited, cnt])
    while (dq):
        temp_dq = dq.popleft()
        for i in range(len(dungeons)):
            k = temp_dq[0]
            visited = temp_dq[1].copy()
            cnt = temp_dq[2]
            if k >= dungeons[i][0] and not visited[i]:
                k -= dungeons[i][1]
                visited[i] = True
                cnt += 1
                dq.append([k, visited, cnt])

    return cnt
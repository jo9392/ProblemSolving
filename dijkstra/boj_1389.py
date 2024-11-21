import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())

relationship_dict = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    relationship_dict[a].append(b)
    relationship_dict[b].append(a)

min_bacon = 100*200
idx = 200

for i in range(1, n+1):
    dp = [100*200]*(n+1)  #최단 경로
    dq = deque()
    dq.append([i,0])
    while(dq):
        pos, cost = dq.popleft()
        for next_pos in relationship_dict[pos]:
            if dp[next_pos] > cost+1:    #최단 경로 갱신 시
                dp[next_pos] = cost+1
                dq.append([next_pos, cost+1])
    dp[0] = 0
    dp[i] = 0
    if sum(dp) < min_bacon:
        min_bacon = sum(dp)
        idx = i

    
print(idx)



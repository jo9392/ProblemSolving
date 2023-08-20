from collections import deque
n, k = map(int, input().split())
dq = deque([[k, 0]])
min_ans = abs(n-k)
visited = [0]*(200000)
while(dq):
    temp_k, ans = dq.popleft()
    if ans + 1 <= min_ans:
        if temp_k > n:
            if not visited[temp_k+1]:
                visited[temp_k+1] = 1
                dq.append([temp_k + 1, ans + 1])
            if not visited[temp_k-1]:
                visited[temp_k-1] = 1
                dq.append([temp_k - 1, ans + 1])
            if temp_k % 2 == 0:
                if not visited[int(temp_k/2)]:
                    visited[int(temp_k/2)] = 1
                    dq.append([int(temp_k/2), ans + 1])
        else:
            min_ans = min(min_ans, ans+(n-temp_k))
    else:
        pass

print(min_ans)
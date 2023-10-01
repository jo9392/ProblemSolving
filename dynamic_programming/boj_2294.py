import sys
from collections import deque
input = sys.stdin.readline


n, k = map(int, input().split())
num_list = set()
for i in range(n):
    num_list.add(int(input()))
num_list = list(num_list)
num_list.sort(reverse=True)
num_list = deque(num_list)

while(num_list):
    if num_list[0] > k:
        num_list.popleft()
    else:
        break

dp = list(20000 for _ in range(k+1))
dp[0] = 0

for n in num_list:
    for i in range(n, k+1):
        dp[i] = min(dp[i], dp[i-n]+1)

if dp[k] == 20000:
    print(-1)
else:
    print(dp[k])
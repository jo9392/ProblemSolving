import sys
input=sys.stdin.readline

[N, K] = list(map(int,(input().split())))
item_list = list()
for i in range(N):
    item_list.append(list(map(int,(input().split()))))

dp = [0]*(K+1)

for w, v in item_list:
    for j in range(w, K+1):
        dp[j] = max(dp[j], dp[j-w]+v)

print(dp[K])
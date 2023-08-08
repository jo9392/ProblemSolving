import sys
input = sys.stdin.readline
import copy

n, m = map(int, input().split())
tomato_box = list()
dp = list()
dp.append([9999999]*(n+1))
for i in range(m):
    temp_str = '-1 '+input()[:-1]+' -1'
    temp_list = list(map(int, temp_str.split()))
    temp_dp = list(map(int, temp_str.replace('-1', '9999999').replace('0','2000000').replace('1','0').split()))
    dp.append(temp_dp)
    tomato_box.append(temp_list)
dp.append([9999999]*(n+1))

count = 0
temp_dp = 0
next_dp = 1
while(temp_dp != next_dp):
    temp_dp = copy.deepcopy(dp)
    count += 1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if dp[i][j] == 9999999:
                continue
            else:
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i+1][j]+1, dp[i][j+1]+1, dp[i][j])
    next_dp = copy.deepcopy(dp)

dp = dp[1:-1]
dp = [i[1:-1] for i in dp]
answer = max(sum(dp, []))
if answer >= 1000000:
    print(-1)
else:
    print(answer)
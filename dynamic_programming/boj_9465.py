import sys
input = sys.stdin.readline

k= int(input())
for i in range(k):
    m = int(input())
    num_list = list()
    for j in range(2):
        num_list.append(list(map(int, input().split())))
    dp = [[0]*m for _ in range(2)]
    dp[0][0] = num_list[0][0]
    dp[1][0] = num_list[1][0]
    if m > 1:
        dp[0][1] = num_list[1][0] + num_list[0][1]
        dp[1][1] = num_list[0][0] + num_list[1][1]
    for q in range(2, m):
        for p in range(2):
            if p == 0:
                dp[p][q] = max(dp[1][q-1], dp[1][q-2]) + num_list[p][q]
            else:
                dp[p][q] = max(dp[0][q-1], dp[0][q-2]) + num_list[p][q]
    print(max(dp[0][m-1], dp[1][m-1]))

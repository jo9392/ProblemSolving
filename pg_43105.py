def solution(triangle):
    dp = list()

    for i in range(len(triangle)):
        dp.append([-1]*(i+1))
    dp[0][0] = triangle[0][0]

    for i in range(1,len(triangle)):
        for j in range(i+1):
            # 왼쪽 위만 있는 경우
            if j==0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            # 오른쪽 위만 있는 경우
            elif j==i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            # 왼쪽 위, 오른쪽 위가 있는 경우
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

    answer = max(dp[i])
    return answer
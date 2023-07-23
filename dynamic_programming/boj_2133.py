n = int(input())
dp = list([0]*(n+3))
dp[0] = 1
temp_n = 0
while(temp_n < n):
    temp_n += 2
    temp_value = 0
    for t in range(temp_n-4, -2, -2):
        temp_value += dp[t]
    temp_value *= 2
    temp_value += dp[temp_n-2]*3
    dp[temp_n] = temp_value

print(dp[n])
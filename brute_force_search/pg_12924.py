def solution(n):
    answer = 1
    maximum = n//2 + 1
    for i in range(1, maximum):
        tmp = 0
        j = i
        while(tmp < n):
            tmp += j
            if tmp == n:
                answer += 1
            j += 1
    return answer
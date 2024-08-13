def solution(arr):
    tmp = max(arr)
    while(True):
        flag = 0
        for a in arr:
            if tmp % a != 0:
                flag = 1
                break
        if flag == 0:
            break
        tmp += 1
    answer = tmp
    return answer
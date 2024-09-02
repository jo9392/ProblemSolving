def solution(n, tops):
    v = [0]*(n+1)
    v[0] = 1
    v[1] = 3 + tops[0]
    for i in range(2, n+1):
        v[i] = (v[i-1] * (3 + tops[i-1]) - v[i-2]) % 10007
    answer = v[n]
    return answer
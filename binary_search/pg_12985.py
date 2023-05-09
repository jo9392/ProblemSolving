from math import log2


def solution(n, a, b):
    total_round = int(log2(n))
    k = 0
    start = 0
    end = n
    while (True):
        mid = (start + end) // 2
        if a <= mid and b <= mid:  # 첫번째 구역에 둘 다 포함된다면
            end = mid
        elif a > mid and b > mid:  # 두번째 구역에 둘 다 포함된다면
            start = mid
        else:
            break
        k += 1

    return total_round - k
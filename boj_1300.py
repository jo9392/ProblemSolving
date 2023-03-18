def count_small_num(N, s_num):
    count = 0
    for i in range(1, N + 1):
        count += min(s_num // i, N)
    return count


if __name__ == '__main__':
    N = int(input())
    k = int(input())
    count = 0
    s_num = int(k/2)
    left = 1
    right = k
    while(left <= right):
        count = count_small_num(N, s_num)
        if count >= k:
            right = s_num - 1
        else:
            left = s_num + 1
        s_num = int((left+right)/2)

    print(s_num+1)
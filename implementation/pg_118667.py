from collections import deque


def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    if (sum1 + sum2) % 2 != 0:
        return -1

    while (sum1 != sum2):
        if sum1 > sum2:
            temp_num = queue1.popleft()
            queue2.append(temp_num)
            answer += 1
            sum1 -= temp_num
            sum2 += temp_num
        else:
            temp_num = queue2.popleft()
            queue1.append(temp_num)
            answer += 1
            sum1 += temp_num
            sum2 -= temp_num
        if answer > 600000:
            return -1

    return answer
from collections import deque


def score_compute(a_list, my_list):
    gap = 0
    for i in range(10):
        if a_list[i] == 0 and my_list[i] == 0:
            pass
        else:
            gap = gap - (10 - i) if a_list[i] > my_list[i] else gap + (10 - i)
    return gap


def solution(n, info):
    max_gap = 0
    my_list = [i + 1 for i in info]
    answer_queue = deque([[0 for _ in range(11)]])

    cnt = 0
    answer_list = [[0 for _ in range(11)]]
    while (answer_queue):
        temp_queue = answer_queue.popleft()
        temp_score = score_compute(info, temp_queue)

        if max_gap == temp_score:
            answer_list.append(temp_queue)
        elif max_gap < temp_score:
            max_gap = temp_score
            answer_list = [temp_queue]

        for i in range(10):
            if temp_queue[i] == 0 and sum(temp_queue) + my_list[i] <= n:
                append_queue = temp_queue.copy()
                append_queue[i] = my_list[i]
                answer_queue.append(append_queue)

    answer = answer_list[-1]

    if score_compute(info, answer) <= 0:
        print(answer)
        return [-1]
    else:
        answer[-1] += n - sum(answer)
        return answer
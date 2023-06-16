def solution(n):
    answer = []
    temp_cnt = 0
    while (n >= 1):
        temp_answer = []
        temp_answer.append([1 + temp_cnt])
        if n != 1:
            for i in range(2, n):
                temp_answer.append([i + temp_cnt, 3 * n - 3 - i + 2 + temp_cnt])
            temp_answer.append([i for i in range(n + temp_cnt, 2 * n + temp_cnt)])
        answer.append(temp_answer)
        temp_cnt = 3 * n - 3 + temp_cnt
        n -= 3

    for i in range(len(answer) - 2, -1, -1):
        answer[i] = insert_answer(answer[i], answer[i + 1])
    real_answer = answer.pop(0)
    answer = []
    for r in real_answer:
        answer.extend(r)
    return answer


def insert_answer(list_a, list_b):
    for i in range(2, 2 + len(list_b)):
        temp_pop = list_a[i].pop()
        list_a[i].extend(list_b[i - 2])
        list_a[i].append(temp_pop)
    return list_a
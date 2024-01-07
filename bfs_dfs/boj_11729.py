# 아무거나 때려박다가 실패한 문제.
# 좀 나중에 다시 풀어보자.
from collections import deque
import sys

n = int(input())
init_queue = [[i for i in range(n, 0, -1)],[],[]]
last_queue = [[],[],[i for i in range(n, 0, -1)]]
cnt = 0
dq = deque()
dq.append([init_queue, cnt])

while (dq):
    temp_queue, cnt = dq.popleft()
    first, second, third = temp_queue
    if first == [] and second == [] and third == [i for i in range(n, 0, -1)]:
        answer = cnt
        break
    else:
        lists = [[first, second, third], [second, first, third], [first, third, second], [third, first, second],
                        [second, third, first], [third, second, first]]
        flag = 0
        for a, b, c in lists:
            flag += 1
            a = a.copy()
            b = b.copy()
            c = c.copy()
            # a에서 b로 옮기는 경우
            if a != []:
                a_num = a.pop()
                if b != []:
                    b_num = b.pop()
                    if b_num > a_num:
                        b.append(b_num)
                        b.append(a_num)
                        if flag == 1:
                            dq.append([[a, b, c], cnt + 1])
                        elif flag == 2:
                            dq.append([[b, a, c], cnt + 1])
                        elif flag == 3:
                            dq.append([[a, c, b], cnt + 1])
                        elif flag == 4:
                            dq.append([[b, c, a], cnt + 1])
                        elif flag == 5:
                            dq.append([[c, a, b], cnt + 1])
                        elif flag == 6:
                            dq.append([[c, b, a], cnt + 1])
                else:
                    b.append(a_num)
                    if flag == 1:
                        dq.append([[a, b, c], cnt + 1])
                    elif flag == 2:
                        dq.append([[b, a, c], cnt + 1])
                    elif flag == 3:
                        dq.append([[a, c, b], cnt + 1])
                    elif flag == 4:
                        dq.append([[b, c, a], cnt + 1])
                    elif flag == 5:
                        dq.append([[c, a, b], cnt + 1])
                    elif flag == 6:
                        dq.append([[c, b, a], cnt + 1])
            first, second, third = temp_queue
print(answer)
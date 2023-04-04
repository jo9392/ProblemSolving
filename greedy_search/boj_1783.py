import sys
from collections import deque

if __name__=="__main__":
    input = sys.stdin.readline
    length, width = map(int, input().split())

    pos_change=[(1,2), (2,1), (1,-2), (2,-1)]
    pos = (0,0)
    cnt=1
    dq = deque()
    dq.append([pos, cnt])

    # for i in range(2):
    while(dq):
        temp_dq = dq.popleft()
        for pc in pos_change:
            temp_pos = temp_dq[0]
            temp_cnt = temp_dq[1]
            next_pos = tuple(sum(elem) for elem in zip(temp_pos, pc))
            if 0<=next_pos[0]<width and 0<=next_pos[1]<length:
                temp_cnt += 1
                dq.append([next_pos, temp_cnt])

    print(temp_cnt)
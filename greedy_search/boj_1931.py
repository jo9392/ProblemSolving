from collections import deque
def has_duplicates(seq):
    return len(seq) != len(set(seq))

if __name__ == "__main__":
    node_cnt = int(input())
    all_meet_list = []
    for i in range(node_cnt):
        (x, y) = map(int, input().split())
        all_meet_list.append((x, y))
    sorted_list = sorted(all_meet_list, key=lambda all_meet_list:all_meet_list[1])
    sorted_dq = deque(sorted_list)
    cnt = 0
    end_time = 0
    while(sorted_dq):
        temp_dq = sorted_dq.popleft()
        end_time = temp_dq[1]
        # temp_dq와 겹치는 스케줄을 전부 삭제하는 코드
        for i in range(len(sorted_dq)):
            if sorted_dq[0][0] < end_time:
                sorted_dq.
            else:
                break
        cnt += 1

    print(cnt)
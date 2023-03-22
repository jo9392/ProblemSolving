if __name__ == "__main__":
    node_cnt = int(input())
    meet_list = []
    for i in range(node_cnt):
        (x, y) = map(int, input().split())
        meet_list.append((x, y))

    meet_list.sort(key = lambda meet_list:(meet_list[1], meet_list[0]))
    cnt = end_time = 0

    for i in range(len(meet_list)):
        if meet_list[i][0] >= end_time:
            cnt += 1
            end_time = meet_list[i][1]

    print(cnt)
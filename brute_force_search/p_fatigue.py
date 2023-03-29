def solution(k, dungeons):
    answer = 0
    dungeons_list = []
    for d in dungeons:
        dungeons_list.append((d[0] - d[1], d))

    dungeons_list = sorted(dungeons_list, key=lambda dungeons_list: dungeons_list[0],
                           reverse=True)
    for d in dungeons_list:
        if k >= d[1][0]:
            answer += 1
            k -= d[1][1]
    return answer
# 다익스트라 - 출발 노드로부터의 최단 거리 list를 저장해두고 매번 갱신, 최단거리보다 cost가 많이 나오면 del
# defaultdict(list) - value가 list로 들어갈 수 있는 dictionary 함수. dict[a].append()로 value 추가 가능

from collections import deque, defaultdict


def dijkstra(road, N):
    cost_list = [5000000 for _ in range(N)]
    node_relation = defaultdict(list)
    for a, b, c in road:
        node_relation[a].append((b, c))
        node_relation[b].append((a, c))

    cost_list[0] = 0

    dq = deque([[1, 0]])
    while (dq):
        temp_dq = dq.popleft()
        temp_pos = temp_dq[0]
        temp_cost = temp_dq[1]
        for next_node, next_cost in node_relation[temp_pos]:
            min_cost = cost_list[next_node - 1]
            if next_cost + temp_cost <= min_cost:
                dq.append([next_node, temp_cost + next_cost])
                cost_list[next_node - 1] = next_cost + temp_cost

    return cost_list


def solution(N, road, K):
    answer = 0
    cost_list = dijkstra(road, N)
    for c in cost_list:
        if c <= K:
            answer += 1
    return answer
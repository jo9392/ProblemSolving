import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while(True):
        answer += 1
        food1 = heapq.heappop(scoville)
        if food1 >=K :
            answer -= 1
            break
        if not scoville:
            answer = -1
            break
        food2 = heapq.heappop(scoville)
        new_food = food1 + food2*2
        heapq.heappush(scoville, new_food)

    return answer
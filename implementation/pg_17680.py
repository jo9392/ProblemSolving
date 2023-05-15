# collections import deque
# deque, list는 remove(c)로 특정 원소를 삭제하는 기능이 있다
# deque(maxlen=cacheSize) 쓰면 maxlen을 지정할 수 있다

from collections import deque
def solution(cacheSize, cities):
    cache = deque("" for _ in range(cacheSize))
    answer = 0
    if cacheSize == 0:
        answer = len(cities)*5
    else:
        for c in cities:
            c = c.lower()
            if c in cache:
                cache.remove(c)
                cache.append(c)
                answer += 1
            else:
                cache.popleft()
                cache.append(c)
                answer += 5
    return answer
# 11:53~ 12:02
from collections import deque

def solution(progresses, speeds):
    progress_dq = deque(progresses)
    speed_dq = deque(speeds)
    day_cnt = 0
    answer = []
    while (progress_dq):
        day_cnt += 1
        temp_complete = 0
        while(progress_dq):
            temp_progress = progress_dq.popleft()
            temp_speed = speed_dq.popleft()
            if temp_progress + temp_speed*day_cnt < 100:
                progress_dq.appendleft(temp_progress)
                speed_dq.appendleft(temp_speed)
                break
            else:
                temp_complete += 1
        if temp_complete != 0:
            answer.append(temp_complete)
        
        

    return answer
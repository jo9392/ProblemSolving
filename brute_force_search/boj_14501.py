import sys
input=sys.stdin.readline

n = int(input())
counseling_list = list()
for start_day in range(n):
    duration, money = map(int, input().split())
    if start_day+duration <= n:          #상담 끝나는 일자가 n일보다 뒤면 불가능한 상담이라 삽입하지 않음
        counseling_list.append([start_day+1, duration, money])

answer = 0
if counseling_list == []: print(0)
else:
    for i in range(len(counseling_list)):
        all_counsel_list = [[counseling_list[i]]]
        while(all_counsel_list):
            temp_schedule = all_counsel_list.pop()
            temp_answer = 0
            for t in temp_schedule: temp_answer += t[2]
            answer = max(answer, temp_answer)
            end_time = temp_schedule[-1][0]+temp_schedule[-1][1] -1
            for c in counseling_list:
                if c not in temp_schedule and end_time < c[0]:
                    temp_append = temp_schedule.copy()
                    temp_append.append(c)
                    all_counsel_list.append(temp_append)
    print(answer)
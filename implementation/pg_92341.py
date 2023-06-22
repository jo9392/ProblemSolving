from math import ceil


def solution(fees, records):
    IN_list = []
    OUT_list = []
    time_dic = dict()
    answer = []

    for record in records:
        temp_str = record.split()
        if temp_str[2] == "IN":
            IN_list.append(temp_str[0:2])
            time_dic[temp_str[1]] = 0
        elif temp_str[2] == "OUT":
            OUT_list.append(temp_str[0:2])

    IN_list = sorted(IN_list, key=lambda I: I[1])
    OUT_list = sorted(OUT_list, key=lambda O: O[1])
    time_dic = dict(sorted(time_dic.items()))

    for IN in IN_list:
        temp_num = IN[1]
        out_flag = False
        for OUT in OUT_list:
            if OUT[1] == temp_num:
                in_time = int(IN[0][:2]) * 60 + int(IN[0][-2:])
                out_time = int(OUT[0][:2]) * 60 + int(OUT[0][-2:])
                time = out_time - in_time
                time_dic[temp_num] += time
                OUT_list.remove(OUT)
                out_flag = True
                break
        if out_flag == False:
            in_time = int(IN[0][:2]) * 60 + int(IN[0][-2:])
            out_time = 23 * 60 + 59
            time = out_time - in_time
            time_dic[temp_num] += time

    for t in time_dic.values():
        answer.append(calculate(fees, t))
    return answer


def calculate(fees, time):
    fee = 0
    if time <= fees[0]:  # 기본 요금 구간이라면
        fee = fees[1]
    else:
        time -= fees[0]
        fee = fees[1] + ceil(time / fees[2]) * fees[3]

    return fee
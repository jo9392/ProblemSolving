def solution(s):
    s_list = s.replace("{", "").rstrip("}").split("},")

    tuple_list = list()
    for i in s_list:
        tuple_list.append(i.split(","))

    tuple_list = sorted(tuple_list, key=lambda x: len(x))
    answer = list()
    temp_t = list()
    for t in tuple_list:
        answer.append(int(list(set(t).difference(temp_t))[0]))
        temp_t = t

    return answer
def is_it_right(s):
    count = 0
    flag = True
    while (s != ""):
        s = s.replace("()", "").replace("{}", "").replace("[]", "")
        count += 1
        if count > 500:
            flag = False
            break
    return flag


def solution(s):
    x = len(s)
    answer = 0
    for i in range(x):
        s = s[1:] + s[0]
        if is_it_right(s):
            answer += 1

    return answer
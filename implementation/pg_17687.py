# 진수 변환은 num을 n으로 나눈 몫을 계속 나눠가면서 0이 될때까지 반복
# 나누면서 나오는 나머지가 뒤부터 숫자로 들어감
# %가 나머지 연산, //가 몫 연산

def convert(num, n):
    return_str = ""
    while num > 0:
        temp = num % n
        if temp == 10:
            temp = 'A'
        elif temp == 11:
            temp = 'B'
        elif temp == 12:
            temp = 'C'
        elif temp == 13:
            temp = 'D'
        elif temp == 14:
            temp = 'E'
        elif temp == 15:
            temp = 'F'
        num = num // n
        return_str = str(temp) + return_str

    return return_str


def solution(n, t, m, p):
    all_str = "0"
    for i in range(t * m):
        all_str += convert(i, n)

    answer = ''
    for i in range(t):
        answer += all_str[m * i + p - 1]
    return answer
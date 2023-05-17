# bin() : 10진수-> 2진수
# int() : n진수 -> 10진수
# range(a, b, c) -> a부터 b까지, b는 불포함, c만큼 간격으로
def solution(numbers):
    answer = []
    for n in numbers:
        if n % 2 == 0:
            answer.append(n + 1)
        else:
            str_list = list(bin(n).replace('b', ''))
            for t in range(len(str_list) - 1, -1, -1):
                if str_list[t] == '0':
                    str_list[t] = '1'
                    str_list[t + 1] = '0'
                    break
            bin_str = '0b' + "".join(str_list)
            answer.append(int(bin_str, 2))

    return answer
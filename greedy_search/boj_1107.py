# 최대한 가까운 숫자를 입력, 그 숫자와의 차이를 더해주면 됨 -> 이게 100에서 그냥 +-하는것보다 많으면 100에서 이동하는 것으로 해야함
# - 그럼 어떻게 최대한 가까운 숫자를 입력하는가?
# - > 같은 숫자를 입력하려고함
# 	-> 없다면?
# 		-> 그 숫자보다 큰 숫자 입력
# 			-> 다음 숫자는 가장 작은 숫자 연속 입력
# 		-> 그 숫자보다 작은 숫자 입력
# 			-> 다음 숫자는 가장 크거나 가장 작은 숫자들로 연속 입력
# - 그냥 100에서 이동
# - 최대의 작은 숫자에서 이동
# - 최소의 큰 숫자에서 이동
# - 한 자리수 더 큰 최소 숫자에서 이동
# - 한 자리수 더 작은 최대 숫자에서 이동
import sys
input = sys.stdin.readline

n = int(input().strip())
f = int(input())
broken_list = []
if f != 0:
    broken_list = list(map(int, input().split()))
    broken_list.sort()
not_broken_list = list(set([0,1,2,3,4,5,6,7,8,9])-set(broken_list))
answer_flag = False
if not_broken_list == []:
    print(abs(n - 100))
elif not_broken_list == [0]:
    print(min(abs(n-100), n+1))
else:
    answer_num = 0
    plus_flag = False
    minus_flag = False
    plus_num = minus_num = 999999999
    for i in str(n):
        if int(i) not in broken_list:
            answer_flag = True
            answer_num = int(i) + answer_num * 10
        else:
            temp_num = 1
            while(temp_num <= 9):
                if int(i)+temp_num in not_broken_list or int(i)-temp_num in not_broken_list:
                    break
                temp_num += 1
            if int(i)+temp_num in not_broken_list:
                plus_num = answer_num*10 + int(i)+temp_num
                plus_flag = True
                add_count = len(str(n)) - len(str(plus_num))
            if int(i)-temp_num in not_broken_list:
                minus_num = answer_num * 10 + int(i) - temp_num
                minus_flag = True
                add_count = len(str(n)) - len(str(minus_num))
            if plus_flag or minus_flag:
                break

    if plus_flag:
        for i in range(add_count):
            plus_num = plus_num * 10 + not_broken_list[0]
    if minus_flag:
        for i in range(add_count):
            minus_num = minus_num * 10 + not_broken_list[-1]


    max_num = 0
    min_num = -999999999
    if not_broken_list[0] != 0:
        for i in range(len(str(n))+1):
            max_num = not_broken_list[0] + max_num*10
    else:
        max_num = not_broken_list[1]
        for i in range(len(str(n))):
            max_num = not_broken_list[0] + max_num*10

    if len(str(n)) > 1:
        min_num = 0
        for i in range(len(str(n)) - 1):
            min_num = not_broken_list[-1] + min_num * 10

    answer = min(abs(n-100), abs(plus_num)-n+len(str(plus_num)), abs(n-minus_num)+len(str(minus_num)), max_num-n+len(str(max_num)), n-min_num+len(str(min_num)))
    if answer_flag:
        answer = min(answer, abs(answer_num-n)+len(str(answer_num)))
    print(answer)
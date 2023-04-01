import sys
import re

input=sys.stdin.readline
bracket_list=input().replace('\n','')

# 옳은 문자열인지 탐색
# ()와 []를 계속 제거
# 제거할 수 없는 시점에서 null 이 아니면 0 출력 후 종료
# 그렇지 않으면 계산

def is_it_wrong():
    temp_string=bracket_list
    while(1):
        if '()' not in temp_string and '[]' not in temp_string:
            break
        temp_string=temp_string.replace('()','').replace('[]','')
    return 1 if temp_string else 0

def plus(bracket_string):
    for b in bracket_string:
        b

if __name__=="__main__":
    if is_it_wrong():
        print(0)
    else:
        bracket_list = bracket_list.replace('()','#2#').replace('[]','#3#')
        # 만약 숫자가 붙어있다면 더해준다
        bracket_list = bracket_list.replace('##','+')
        if '+' in bracket_list:

        # 만약 괄호 안에 숫자가 들어있다면 곱해준다
        bracket_list = bracket_list.replace('(# ... #)', '#...#*3')
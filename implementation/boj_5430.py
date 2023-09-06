import sys
from collections import deque
input = sys.stdin.readline

def solution(func, arr):
    reverse_flag = False
    output = ""

    for f in func:
        if f == 'R':
            reverse_flag = not reverse_flag
        else:
            if len(arr) == 0:
                print("error")
                return
            if reverse_flag:
                arr.pop()
            else:
                arr.popleft()

    arr = list(arr)
    if reverse_flag:
        arr = arr[::-1]
    if arr != []:
        output = "["
        for a in arr:
            output += a + ','
        output = output[:-1]+']'
    else:
        output = '[]'
    print(output)

t = int(input())
for i in range(t):
    func = input()[:-1]
    arr_cnt = int(input())
    arr_input = input()
    if arr_input == '[]\n':
        arr = []
    else:
        arr = deque(arr_input[1:-2].split(','))
    solution(func, arr)

input_num = int(input())

if input_num == 1: print(1)
else:
    temp_input = input_num - 2
    for i in range(1, 999999999):
        temp_input -= 6*(i-1)
        if temp_input < 0: break
    print(i)
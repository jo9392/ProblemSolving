n = int(input().strip())
max_5 = n//5
answer = 5000
for i in range(max_5, -1, -1):
    temp_num = n - i*5
    if temp_num % 3 == 0:
        answer = min(answer, i+temp_num//3)
        break

if answer == 5000:
    answer = -1
print(answer)
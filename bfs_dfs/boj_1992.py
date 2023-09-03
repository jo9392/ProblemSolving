import sys
input = sys.stdin.readline

n = int(input())
table_list = list()
for i in range(n):
    table_list.append(list(map(int, input()[:-1])))
global answer
answer = ''

def quad_squeeze(table, n, a, b):
    global answer
    start = table[a][b]
    for i in range(n):
        for j in range(n):
            if table[a+i][b+j] != start:
                n //= 2
                answer += '('
                quad_squeeze(table, n, a, b)
                quad_squeeze(table, n, a, b+n)
                quad_squeeze(table, n, a+n, b)
                quad_squeeze(table, n, a+n, b+n)
                answer += ')'
                return

    answer += str(start)

quad_squeeze(table_list, n, 0, 0)
print(answer)
import sys


input = sys.stdin.readline
n = int(input().strip())
parent_list = list(map(int, input().split()))
child_list = [[] for _ in range(n)]
for i in range(0, n):
    if parent_list[i] == -1:
        continue
    child_list[parent_list[i]].append(i)

def delete_node(node):
    delete_list = child_list[node]
    child_list[node] = [-1]
    for d in delete_list:
        delete_node(d)

d_node = int(input().strip())
if parent_list[d_node] == -1:   #지우려는 노드가 루트 노드일 경우
    print(0)
else:
    child_list[parent_list[d_node]].remove(d_node)
    delete_node(d_node)

    answer = 0
    for c in child_list:
        if c == []:
            answer += 1

    print(answer)
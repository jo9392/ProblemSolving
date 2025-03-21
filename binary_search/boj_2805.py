import sys

input = sys.stdin.readline

tree_cnt, tree_len = map(int, input().split())
tree_list = list(map(int, input().split()))

left = 0
right = max(tree_list)

while(left <= right):
    mid = (left+right)//2
    temp_len = 0
    for tree in tree_list:
        if tree-mid >0:
            temp_len += (tree-mid)
    if temp_len < tree_len:
        right = mid-1
    elif temp_len >= tree_len:
        left = mid+1
print(left, mid, right)
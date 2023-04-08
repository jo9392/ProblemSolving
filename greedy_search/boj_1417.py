import sys


input = sys.stdin.readline
n = int(input())
candidate1 = int(input())
vote_list = []
if n > 1:
    for _ in range(n-1):
        vote_list.append(int(input()))
    vote_list.sort(reverse=True)

    temp_voter = candidate1
    while(candidate1 <= vote_list[0]):
        candidate1 += 1
        vote_list[0] -= 1
        vote_list.sort(reverse=True)

    print(candidate1-temp_voter)

else:
    print(0)
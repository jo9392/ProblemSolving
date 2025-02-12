from itertools import combinations

n, m = map(int, input().split())

combinations = list(combinations(range(1, n+1), m))
for combination in combinations:
    print(str(combination)[1:-1].replace(",", ""))

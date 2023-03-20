from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
maxnum = 0

for i in list(combinations(arr, 3)):
    _sum = 0
    for j in i:
        _sum += j
    if _sum > maxnum and _sum <= m:
        maxnum = _sum
    
print(maxnum)


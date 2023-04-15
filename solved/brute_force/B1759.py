#암호 : 최소 한 개의 모음 + 최소 두 개의 자음
from itertools import combinations

l, c = map(int, input().split())
arr = list(input().split())

con = [] #자음
vow = [] #모음
arr.sort()
for i in arr:
    if i in ["a", "i", "e", "o", "u"]:
        con.append(i)
    else:
        vow.append(i)

total = []
for i in range(1, l):
    j = l-i
    if j < 2:
        break
    for k in list(combinations(con, i)):
        for r in list(combinations(vow,j)):
            total.append(k+r)

total2 = []
for t in total:
    t = sorted(list(t))
    total2.append("".join(t))

total2.sort()
for t in total2:
    print(t)

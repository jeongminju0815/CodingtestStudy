def backtrack(num , m):
    if len(num) == m:
        print(" ".join(num))
        return 
    for i in range(1, n+1):
        if int(num[-1]) > i:
            continue
        backtrack(num+[str(i)], m)

n, m = map(int, input().split())

for i in range(1, n+1):
    backtrack([str(i)], m)
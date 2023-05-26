n, m = map(int, input().split())
go = []
back = []

for i in range(n):
    start, end = map(int, input().split())

    if start <= end:
        go.append((start,end))
    else:
        back.append((start,end))

go.sort(key = lambda x:(x[0], x[1]))
back.sort(key = lambda x:(-x[0], -x[1]))

go_max = 0
back_min = m
result = 0

for s, e in go:
    if e > go_max:
        if s > go_max:
            result += (e-s)
        else:
            result += (e-go_max)
        go_max = e

for s, e in back:
    result += (back_min - e)
    back_min = e
result += go[0][0]
print(result)




    
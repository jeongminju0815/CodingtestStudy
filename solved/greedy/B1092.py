n = int(input())
cran = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

cran.sort(reverse=True)
box.sort(reverse=True)

time = 0

if cran[0] < box[0]:
    print(-1)
else:
    while len(box) > 0:
        for c in cran:
            for b in box:
                if c >= b:
                    box.remove(b)
                    break
        time += 1
print(time)


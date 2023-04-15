import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())
arr = [0]
if n!= 0:
    arr.extend(list(map(int, input().split())))
arr.append(l)
arr.sort()

end = l-1
start = 1

distance = []
for i in range(n+1):
    value = arr[i+1] - arr[i]
    distance.append(value)


while start<=end:
    mid = (start+end) // 2
    count = 0
    for d in distance:
        if mid == 0:
            continue
        if d > mid:
            count += (d // mid)
            res = d % mid

            if res == 0:
                count -= 1

        if count > m:
            break
    if count > m:
        start = mid + 1
        
    else: #최대 거리가 mid일때 m개 심을 수 있는 경우
        result = mid
        end = mid -1
print(result)
        




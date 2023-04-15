n, c = map(int,input().split())
arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort()
start = 1
end = arr[-1] - arr[0]
result = 0

while start<=end:
    mid = (start+end) // 2
    pivot = arr[0]
    count = 1 #와이파이사이 최대 거리가 넘는개 몇개인지

    for i in range(n):
        if arr[i] >= pivot + mid:
            count += 1
            pivot = arr[i]
    
    if count < c:
        end = mid -1
    else:
        result = mid
        start = mid + 1
print(result)

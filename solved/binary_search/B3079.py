n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(int(input()))

mx = max(arr)
start = 0
end = mx * m
mid = (start + end) // 2
result = end

while start<=end:
    count = 0
    for i in range(len(arr)):
        count += (mid // arr[i])
    if count < m:
        start = mid +1
    else:
        result = min(result, mid)
        end = mid -1
    mid = (start+end) // 2
print(result)


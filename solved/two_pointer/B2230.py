n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort()
right = 0
left = 0
total = arr[n-1] - arr[0]

while left <= right:
    temp = arr[right] - arr[left]
    if temp >= m:
        total = min(total, temp)
        left += 1
    else:
        right += 1
        if right >=n:
            break
print(total)


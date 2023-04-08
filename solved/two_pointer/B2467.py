import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))

right = n-1
left = 0
total = abs(arr[left]+arr[right])
idx = [-1,-1]

while right!=left:
    if abs(arr[left] + arr[right]) <= abs(total):
        total = arr[left] + arr[right]
        idx[0] = left
        idx[1] = right
        if total == 0:
            break
    if abs(arr[left]) >= abs(arr[right]):
        left += 1
    else:
        right -= 1
for i in idx:
    print(arr[i], end=" ")

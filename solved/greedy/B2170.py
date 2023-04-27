import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(tuple(map(int, input().split())))

arr.sort(key=lambda x:(x[0],x[1]))
result = 0
y_max = arr[0][0]

for i in range(n):
    if y_max > arr[i][0]:
        if y_max < arr[i][1]:
            result += (arr[i][1] - y_max)
            y_max = arr[i][1]
    else:
        if y_max < arr[i][1]:
            result += (arr[i][1] - arr[i][0])
            y_max = arr[i][1]
print(result)
n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0
result = arr[0]
count = 0

while left < n:
    if result < m:
        right += 1
        if right >=n:
            break
        result += arr[right]
    elif result >= m:
        if result == m:
            count+=1
        result -= arr[left]
        left+=1
    if left == right:
        if result == m:
            count+=1
        right += 1
        if right >=n:
            break
        result += arr[right]
        
print(count)
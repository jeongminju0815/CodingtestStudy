n,pivot = map(int,input().split())
array = list(map(int,input().split()))

start = 0
end = max(array) - min(array)
answer = 0
while start<=end:
    mid = (start+end)//2
    cnt=1
    min_value=array[0]
    max_value=array[0]

    for i in range(1, n):
        if array[i] > max_value:
            max_value = array[i]
        if array[i] < min_value:
            min_value = array[i]
        check = max_value - min_value
        if check > mid:
            cnt += 1
            min_value = array[i]
            max_value = array[i]
        if cnt > pivot:
            break
    if cnt <= pivot:
        answer = mid
        end = mid-1
        
    else:
        start = mid+1
print(answer)
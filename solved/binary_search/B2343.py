n, m = map(int,input().split())
arr = list(map(int,input().split()))


end = sum(arr)
vm = max(arr) #비디오 최대값
start = vm
mid = (start+end) //2
result = 10**9

while start<=end:
    temp = 1 #블루레이 개수 세주기
    total = 0
    for i in range(n):
        if total+arr[i] > mid: #다음 넣을 강의가 블루레이 크기보다 크다면
            temp += 1 #블루레이 하나 더 생성
            if temp > m: #블루레이 개수 보다 많으면 멈추기
                break
            total = 0
        total += arr[i]
    if temp > m: #블루레이 부족
        #크기 늘림
        start = mid + 1
    else:#블루레이 넉넉
        #크기 줄임
        result = min(result, mid) #넉넉한 크기 중 최소
        end = mid-1
    mid = (start+end) // 2
print(result)





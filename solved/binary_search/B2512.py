def binary_search(arr, start, _dif, diff): #총 배열, 이중 탐색 할 개수,
    mid = start // 2
    
    if _dif - (mid * 2) >= diff:
        print("===arr===")
        print(arr[0], mid)
        return arr[0] + mid
    else:
        binary_search(arr, mid, _dif, diff)


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
money = int(input())
total = sum(arr)
diff = money - total
print("차이:", diff)
if diff >= 0:
    print(arr.max())
else:
    diff = abs(diff)
    i = 1
    while i!=0:
        for i in range(len(arr)-1, -1, -1): #슬라이싱 기준
            _dif = 0
            start = 0
            print("=====")
            for j in range(i+1, len(arr)):
                print(j,i)
                if j == i+1:
                    start = arr[j] - arr[i]
                _dif += (arr[j] - arr[i])
                print(_dif)
            if _dif >= diff:
                print("====result===")
                print(binary_search(arr[i:], start, _dif,diff))







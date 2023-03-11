n = int(input())

for i in range(n):
    test = int(input())
    arr = list(map(int, input().split()))
    money = int(input())

    temp = [0] * (money+1)
    temp[0] = 1
    for j in arr:
        for m in range(j, money+1):
            temp[m] += temp[m-j]
    print(temp[money])




    

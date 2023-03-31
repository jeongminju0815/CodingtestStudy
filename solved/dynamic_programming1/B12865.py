from itertools import combinations

n, k = map(int, input().split())
arr = [(0,0)]
knapsack = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(n):
    w, v = map(int, input().split())
    arr.append((w,v))

for i in range(1, n+1): # 물건 종류
    w, v= arr[i][0], arr[i][1]
    for j in range(1, k+1): # 가방 수용 무게 : j
        if w > j: #물건이 가방 수용 무게보다 클 때
            knapsack[i][j] = knapsack[i-1][j] #이전 물건 dp값 적용
        else: #물건이 가방 수용 무게보다 작을 때
            #해당 물건을 넣었을 때와 안 넣을 때 비교, 넣는경우는 이전 물건 dp에서 (가방 수용 무게 - 현재 물건 무게)크기의 가방 수용 무게일 때 최대 가치 값 
            knapsack[i][j] = max(v+knapsack[i-1][j-w], knapsack[i-1][j]) 
print(knapsack[n][k])


        

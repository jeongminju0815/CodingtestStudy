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
            knapsack[i][j] = knapsack[i-1][j] #이전 물건 dp값 가져옴
        else:
            knapsack[i][j] = max(v+knapsack[i-1][j-w], knapsack[i-1][j])
print(knapsack[n][k])
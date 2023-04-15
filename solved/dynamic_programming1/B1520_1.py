def dfs(row, col):
    global n, m
    if row == n-1 and col == m-1:
        return 1
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    if dp[row][col] != -1:
        return dp[row][col]
    ways = 0
    for i in range(4):
        nx = dx[i] + row
        ny = dy[i] + col

        if 0<=nx<n and 0<=ny<m and arr[row][col] > arr[nx][ny]: #탐색 가능한 조건
            ways += dfs(nx,ny)
    dp[row][col] = ways 
    return dp[row][col]

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
dp = [[-1 for i in range(m)] for i in range(n)]
dfs(0, 0)
print(dp[0][0])
print(dp)
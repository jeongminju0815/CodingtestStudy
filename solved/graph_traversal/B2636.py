from collections import deque, defaultdict

def bfs(row, col):
    global prefix

    q = deque([])
    q.append([row,col])
    visited[row][col] = True

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    while q:
        r, c = q.popleft()
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if arr[nx][ny] == 1:
                    visited[nx][ny] = True
                    arr[nx][ny] = 0
                    prefix -= 1
                else:
                    q.append([nx,ny])
                    visited[nx][ny] = True
    return prefix

n, m = map(int, input().split())
arr = []
prefix = 0

for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(m):
        if arr[i][j] == 1:
            prefix += 1
            
count = [prefix]

while True:
    visited = [[False for _ in range(m)] for _ in range(n)]
    count.append(bfs(0,0))#탐색

    if count[-1] == 0:
        break
print(len(count)-1)
print(count[-2])
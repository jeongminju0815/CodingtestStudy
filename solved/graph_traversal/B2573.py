from collections import deque
import sys
sys.setrecursionlimit(10**6)

def bfs(row,col):
    visited[row][col] = True
    q = deque()
    q.append([row,col])

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while q:
        r, c = q.popleft()
        sea = 0
        for i in range(4):
            nx = dx[i] + r
            ny = dy[i] + c

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if arr[nx][ny] == 0:
                    sea += 1
                else:
                    q.append([nx,ny])
                    visited[nx][ny] = True  
        ice.add((r,c,sea))

    return 1

n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
time = 0
while True:
    visited = [[False]*m for i in range(n)]
    count = 0
    ice = set()
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0 and not visited[i][j]:
                count += bfs(i,j) #0이 아닌 곳 탐색
    if count == 0:
        print(0)
        break
    for r, c, s in ice:
        arr[r][c] -= s
        if arr[r][c] < 0:
            arr[r][c] = 0
    time += 1
    if count >=2:
        print(time-1)
        break

    
            
        
        

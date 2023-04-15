from collections import deque

def bfs(row, col):
    q = deque([])
    q.append([row,col])
    visited[row][col] = True

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    belt = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            nx = dx[i] + r
            ny = dy[i] + c

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    visited[nx][ny] = True
                    belt += 1
                else:
                    q.append([nx,ny])
                    visited[nx][ny] = True
    return belt


n, m = map(int, input().split())
arr = []
ctotal = 0
time = 0

for i in range(n):
    temp = list(map(int,input().split()))
    arr.append(temp)
    ctotal += temp.count(1)

bctotal = 0

while True:
    if ctotal == 0:
        break
    visited = [[False] * (m) for i in range(n)]
    bctotal = bfs(0,0)
    ctotal -= bctotal
    time += 1

print(time)
print(bctotal)
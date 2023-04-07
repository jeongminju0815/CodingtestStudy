from collections import deque

def bfs(row,col):
    global max_distance

    visited[row][col] = 1
    q = deque([])
    q.append([row,col])

    while q:
        r, c = q.popleft()
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        for i in range(4):
            nx = dx[i] + r
            ny = dy[i] + c

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if map[nx][ny] == "L":
                    q.append([nx,ny])
                    visited[nx][ny] = visited[r][c] + 1

                    if max_distance < visited[nx][ny]:
                        max_distance = visited[nx][ny]

n, m = map(int, input().split())
map = [input() for _ in range(n)]
max_distance = 0

for i in range(n):
    for j in range(m):
        visited = [[0 for _ in range(m)] for _ in range(n)]
        if map[i][j] == "L":
            bfs(i,j)

print(max_distance-1)


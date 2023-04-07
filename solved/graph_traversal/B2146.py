from collections import deque

def dfs(row,col):
    global ground

    visited[row][col] = True

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in range(4):
        nx = dx[i] + row
        ny = dy[i] + col

        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
            if map[nx][ny] == 1:
                visited[nx][ny] = True
                map[nx][ny] += ground
                dfs(nx,ny)

def bfs(row, col,near_ground):
    visited[row][col] = True
    q = deque([])
    q.append([row,col,near_ground])
    distance[row][col] += 1

    while q:
        r, c, ng = q.popleft()
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        for i in range(4):
            nx = dx[i] + r
            ny = dy[i] + c

            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if map[nx][ny] != 0:
                    if map[nx][ny] != near_ground:
                        continue
                    else:
                        distance[r][c] = 1
                        print(nx,ny) #여기가 실행이 왜 안되징
                else:
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[r][c] + 1
                    q.append([nx,ny,near_ground])



# dfs로 구역 나눠주고
# bfs로 섬까지 거리 탐색
n = int(input())
map = [list(map(int, input().split())) for i in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
print(map)
ground = 1

for i in range(n):
    for j in range(n):
        if map[i][j] == 1 and not visited[i][j]:
            map[i][j] += ground
            dfs(i,j)
            print(map)
            ground += 1 

visited = [[False for _ in range(n)] for _ in range(n)]
distance = [[0 for _ in range(n)] for _ in range(n)]
near_ground = -1 #현재 가장 가까운 섬

for i in range(n):
    for j in range(n):
        if map[i][j] != 1:
            near_ground = map[i][j]
        if map[i][j] == 0 and not visited[i][j]:
            bfs(i,j,near_ground)
            print(distance)
print(distance)                 
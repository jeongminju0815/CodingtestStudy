from collections import deque
import sys
sys.setrecursionlimit(10**6)

def bfs(row,col):
    visited[row][col] = True
    q = deque([])
    q.append([row,col])
                

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    while q:
        r,c = q.popleft()
        sea = 0
        for i in range(4):
            nx = dx[i] + r
            ny = dy[i] + c

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if arr[nx][ny] <=0: #바다라면
                    sea += 1 #주변 바다 개수 추가
                else:#빙산일 때
                    visited[nx][ny] = True
                    q.append([nx,ny])
        if sea > 0: #탐색한 경로 중 바다가 있었다면
            near_sea.append([r,c,sea]) #x,y,주변 바다 개수

    return 1



n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

# 빙산 위치 리스트
ice = []
for i in range(n):
    for j in range(m):
        if arr[i][j] != 0:
            ice.append((i,j))


remove_ice = []
time = 0

while ice:
    visited = [[False for _ in range(m)] for _ in range(n)]
    ice_group = 0
    near_sea = []
    for i, j in ice:
        if arr[i][j] > 0 and not visited[i][j]: #방문하지 않은 빙산
            ice_group += bfs(i,j)
    if ice_group >=2:
        print(time)
        break
    for i, j,sea in near_sea:
        arr[i][j] -= sea
        if arr[i][j] <=0:
            remove_ice.append((i,j))
    ice = sorted(list(set(ice) - set(remove_ice)))#더이상 빙산이 아닌 것들 빼줌

    time += 1

if ice_group < 2:
    print(0)
    
            
        
        

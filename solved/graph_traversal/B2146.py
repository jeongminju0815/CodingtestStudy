import sys
from collections import deque
sys.setrecursionlimit(10**6)

num = int(input())
arr = [list(map(int,input().split())) for _ in range(num)]

ans = sys.maxsize

def dfs(i,j):
    global cnt
    if i < 0 or i >= num or j < 0 or j >= num:
        return False
    if arr[i][j] == 1:
        arr[i][j] = cnt
        for x,y in (0,1),(0,-1),(1,0),(-1,0):
            nx = x+i
            ny = y+j
            dfs(nx,ny)
        return True

def bfs(n):
    global ans
    check = [[-1] * num for _ in range(num)] #방문하지 않은 것 확인
    q = deque()

    for i in range(num):
        for j in range(num):
            if arr[i][j] == n: #탐색하려는 섬 n의 좌표 넣어주기
                q.append((i,j))
                check[i][j] = 0 #방문함과 동시에 거리 0 으로 초기화
    while q:
        x,y = q.popleft()
        for a,b in (0,-1),(0,1),(1,0),(-1,0):
            nx = x+a
            ny = y+b
            if nx < 0 or nx >= num or ny < 0 or ny >= num:
                continue
            #다른 섬에 도착한 경우
            if arr[nx][ny] > 0 and arr[nx][ny] != n:
                ans = min(ans,check[x][y])
                return
            #바다이고, 방문한 적이 없다면
            if arr[nx][ny] == 0 and check[nx][ny] == -1:
                check[nx][ny] = check[x][y]+1
                q.append((nx,ny))
    print(check)

cnt = 2
for i in range(num):
    for j in range(num):
        if dfs(i,j) == True:
            cnt+=1
print(arr)
for i in range(2,cnt): #섬개수마다 최단거리 확인
    bfs(i)

print(ans)
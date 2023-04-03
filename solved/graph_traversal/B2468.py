from collections import deque

def bfs(row, col, h):
    q = deque([])
    q.append([row,col, h])
    visited[row][col] += 1

    while q:
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        r, c, h = q.popleft()
        # print(r,c,h)
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]

            if 0<=nx<n and 0<=ny<n and visited[nx][ny] <= h:
                if arr[nx][ny] <= h:
                    continue
                q.append([nx,ny,h])
                visited[nx][ny] += 1
    # print("방문완료",row,col, visited, h)
    return 1

n = int(input())
arr_max = 0
arr = []
result = 0

for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

    if max(temp) > arr_max:
        arr_max = max(temp)
# print(arr)
visited = [[0 for _ in range(n)] for _ in range(n)] #높이가 h일때 탐색할 수 있는지 h 값으로 기록
for h in range(arr_max+1): #0~최대높이까지
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == h and arr[i][j] > h:
                cnt += bfs(i, j, h)
                # print("cnt", cnt, h)
    if cnt > result:
        result = cnt

print(result)





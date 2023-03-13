from collections import deque

def bfs():
    q = deque([[7,0,0]])
    check[7][0] = True
    dx = [1,-1,0,0,-1,1,-1,1,0]
    dy = [0,0,1,-1,-1,1,1,-1,0]

    while q:
        x, y, count = q.popleft()
        if count == 7:
            if x==7-count and y == 7:
                print("탈출")
                return 1
        for i in range(9):
            nx = dx[i] + x
            ny = dy[i] + y
            print(nx,ny)
            print(q)
            if nx < 0 or ny < 0 or nx>= 8 or ny >=8 or nx-1<0:
                continue
            if arr[nx][ny] == "#":
                continue
            if check[nx][ny]:
                continue
            q.append([nx,ny,count+1])
            check[nx][ny] = True
    return 0

arr = [input() for i in range(8)]
check = [[False for i in range(8)] for _ in range(8)]
print(arr)
print(check)
print(bfs())
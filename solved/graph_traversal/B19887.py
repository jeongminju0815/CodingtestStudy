import sys
input = sys.stdin.readline

def bfs():
    global ans
    q = set([(0,0,arr[0][0])]) #(행, 열, 값)

    while q:
        row, col, ways = q.pop() #집합의 pop은 아무원소나 삭제
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        ans = max(ans, len(ways))

        for i in range(4):
            nx = dx[i] + row
            ny = dy[i] + col

            if 0<=nx<r and 0<=ny<c:
                if arr[nx][ny] not in ways:
                    q.add((nx,ny,ways+arr[nx][ny]))

r, c = map(int, input().split())
arr = [input() for i in range(r)]
ans = 0
bfs()

print(ans)
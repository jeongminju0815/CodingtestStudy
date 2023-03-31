import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(row, col):
    if dp[row][col] != 0: #이전에 탐색했다면
        return dp[row][col] #여기서부턴 최대의 탐색 기록으로 탐색하지 않아도 됨

    nx = [1,-1,0,0]
    ny = [0,0,1,-1]

    for i in range(4):
        dx = nx[i] + row
        dy = ny[i] + col
        if 0<=dx<n and 0<=dy<n and arr[dx][dy] > arr[row][col]: #이동하려는 값이 더 클때만 이동가능
            dp[row][col] = max(dfs(dx, dy) , dp[row][col]) #탐색한 값과 기존 값을 비교하여 최대 값 업데이트

    dp[row][col] += 1 #자기자신 이동하는 경우
    return dp[row][col] 



n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
max_move = 0

for i in range(n):
    for j in range(n):
        if dp[i][j] == 0: #도착 장소가 정해져있지 않아 모든 경로 탐색
            dfs(i,j)

for i in range(n):
    for j in range(n):
        if dp[i][j] > max_move:
            max_move = dp[i][j]
print(max_move)

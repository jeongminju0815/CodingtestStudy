from copy import deepcopy
import sys

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1) #북동남서
types = ( #dx,dy의 위치 좌표
    (),
    ([0], [1], [2], [3]),
    ((0, 2), (1, 3)),
    ((0, 1), (1, 2), (2, 3), (0, 3)),
    ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)),
    [(0, 1, 2, 3)],
)
ans = sys.maxsize

cctvs = []
for i in range(n):
    for j in range(m):
        if 0 < graph[i][j] < 6:
            cctvs.append((i, j))


def dfs(graph, depth):
    global ans

    if depth == len(cctvs):
        ans = min(ans, sum([row.count(0) for row in graph]))
        return

    x, y = cctvs[depth] #cctv좌표
    for dirs in types[graph[x][y]]:
        temp_graph = deepcopy(graph)

        for dir in dirs:
            nx, ny = cctvs[depth] #depth번째 cctv
            print(depth, cctvs)

            while True:
                nx, ny = nx + dx[dir], ny + dy[dir]
                if not 0 <= nx < n or not 0 <= ny < m:
                    break
                if temp_graph[nx][ny] == 6:
                    break
                if temp_graph[nx][ny] == 0:
                    temp_graph[nx][ny] = 7
        dfs(temp_graph, depth + 1)


dfs(graph, 0)
print(ans)
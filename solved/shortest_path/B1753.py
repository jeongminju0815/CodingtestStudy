import sys
import heapq
input = sys.stdin.readline
INF = 1e9

def dijkstra():
    q = []
    heapq.heappush(q, (0,k))
    path[k] = 0

    while q:
        cost, node = heapq.heappop(q)

        if path[node] < cost:
            continue
        for i in graph[node]:
            n, c = i[0], i[1]
            nd = cost + c
            if path[n] > nd:
                path[n] = nd
                heapq.heappush(q, (nd, n))
            

v, e = map(int, input().split())
k = int(input())

graph = [[] for i in range(v+1)]
path = [INF] * (v+1)

for i in range(e):
    s, e, w = map(int, input().split())
    graph[s].append([e,w])

dijkstra()
for i in range(1,v+1):
    if path[i] == INF:
        print("INF")
    else:
        print(path[i])


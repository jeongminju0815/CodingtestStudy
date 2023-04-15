import heapq
import sys
input = sys.stdin.readline
INF = 1e9

def dijkstra(start):
    global n, x
    q = []
    path = [INF] * (n+1)
    heapq.heappush(q, [0,start])
    path[start] = 0

    while q:
        cost, node = heapq.heappop(q)

        if path[node] < cost:
            continue
        for i in graph[node]:
            _node, c = i[0], i[1]
            if _node != start:
                nd = c + cost
                if path[_node] > nd:
                    path[_node] = nd
                    heapq.heappush(q, (nd, _node))
    if start == x:
        for i in range(1, len(path)):
            sum_path[i] += path[i]
    else:
        sum_path[start] += path[x]

n, m, x = map(int,input().split())
graph = [[] for i in range(n+1)]
sum_path = {i:0 for i in range(1,n+1)}

for i in range(m):
    s,e,t = map(int, input().split())
    graph[s].append([e,t])

for i in range(1,n+1):
    dijkstra(i)
print(max(sum_path.values()))
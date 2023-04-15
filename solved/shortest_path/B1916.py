import heapq
import sys

input = sys.stdin.readline
INF = 1e9

def dijakstra():
    q = []
    heapq.heappush(q, (0, sb))
    path[sb] = 0

    while q:
        cost, node = heapq.heappop(q)

        if path[node] < cost: #이미 최단경로, 같을때는 다른 경로로 올수도 있어서 제외
            continue
        for i in graph[node]:
            nd = i[1] + cost
            if nd < path[i[0]]: #여기도 마찬가지
                path[i[0]] = nd
                heapq.heappush(q, (nd, i[0]))
        print("후",q)
n = int(input()) #도시
m = int(input()) #버스

graph = [[] for i in range(n+1)]
path = [INF] * (n+1)

for i in range(m):
    s, e, c = map(int, input().split())
    graph[s].append([e,c])

sb, eb = map(int, input().split())

dijakstra()
print(path[eb])
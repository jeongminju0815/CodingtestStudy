from collections import deque

def bfs(node):
    visited[node] = True
    q = deque([])
    q.append(node)

    while q:
        p = q.popleft()
        
        for c in graph[p]:
            if not visited[c]:
                visited[c] = True
                parent[c] = p
                q.append(c)

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]

for i in range(n-1):
    n1, n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited = [False] * (n+1)
bfs(1)
for p in parent[2:]:
    print(p)
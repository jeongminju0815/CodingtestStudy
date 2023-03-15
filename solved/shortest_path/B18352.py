from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    check[start] = True
    q = deque([start])
    result = []

    while q:
        node = q.popleft()
        for i in arr[node]:
            if not check[i]:
                check[i] = True
                q.append(i)
                distance[i] = distance[node] +1
                if distance[i] == dist:
                    result.append(i)
                if distance[i] > dist:
                    return result
    return result

n, m, dist, start = map(int, input().split())

arr = [[] for _ in range(n+1)]
check = [False] * (n+1)
distance = [0] * (n+1)

for i in range(1, m+1):
    a, b = map(int, input().split())
    arr[a].append(b)

result = bfs(start)
result.sort()
if len(result) == 0:
    print(-1)
for i in result:
    print(i)


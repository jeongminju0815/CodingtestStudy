import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def find_parent(node):
    if parent[node] != node:
        parent[node] = find_parent(parent[node])
    return parent[node]

def union_parent(n1, n2):
    n1 = find_parent(n1)
    n2 = find_parent(n2)

    if n1 < n2:
        parent[n2] = n1
    else:
        parent[n1] = n2


n = int(input()) #도시 개수
m = int(input()) #여행계획 도시
parent = [i for i in range(n+1)]
edges = [[] for i in range(n+1)]

for i in range(1, n+1):
    temp = list(map(int, input().split()))
    for j in range(1, n+1):
        if temp[j-1] == 1:
            if find_parent(i) != find_parent(j):
                union_parent(i, j)

trip = list(map(int, input().split()))
goal = find_parent(trip[0])
flag = False

for t in trip:
    if goal != find_parent(t):
        print("NO")
        flag = True
        break

if not flag:
    print("YES")

def find_parent(node):
    if parent[node] !=node:
        parent[node] = find_parent(parent[node])
    return parent[node]

def union_parent(n1, n2):
    n1 = find_parent(n1)
    n2 = find_parent(n2)

    if n1 < n2:
        parent[n2] = n1
    else:
        parent[n1] = n2



v, e = map(int, input().split())
parent = [i for i in range(v+1)]
edgs = []

for i in range(e):
    a, b, c = map(int, input().split())
    edgs.append([c,a,b])

edgs.sort()
result = 0

for c, a, b in edgs:
    if find_parent(a) != find_parent(b):
        union_parent(a,b)
        result += c
print(result)

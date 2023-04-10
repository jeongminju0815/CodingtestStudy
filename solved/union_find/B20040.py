import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def find_parent(node):
    if parent[node] != node:
        parent[node] = find_parent(parent[node])
    return parent[node]

def union_parent(node1, node2):
    node1_parent = find_parent(node1)
    node2_parent = find_parent(node2)

    if node1_parent < node2_parent:
        parent[node2_parent] = node1_parent
    else:
        parent[node1_parent] = node2_parent
    return False

n, m = map(int,input().split())
parent = [i for i in range(n)]
flag = False #사이클 발생 여부

for i in range(m):
    n1, n2 = map(int, input().split())
    if find_parent(n1) == find_parent(n2):
        print(i+1)
        flag = True
        break
    union_parent(n1, n2)


if not flag:
    print(0)
    
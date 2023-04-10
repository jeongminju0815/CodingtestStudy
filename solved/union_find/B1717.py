def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a]) #탐색을 줄이기 위해 부모 갱신
    return parent[a] 

def union_parent(a,b):
    a_parent = find_parent(a)
    b_parent = find_parent(b)

    if a_parent < b_parent:
        parent[b_parent] = a_parent
    else:
        parent[a_parent] = b_parent

n, m = map(int,input().split())
parent = [i for i in range(n+1)]

for i in range(m):
    o, a, b = map(int, input().split())

    if o ==0:
        union_parent(a, b)
    elif o ==1:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")

# class Node():
#     def __init__(self, item):
#         self.data = item
#         self.right = None
#         self.left = None
    
# class Tree():
#     def __init__(self):
#         self.root = None

# tree = Tree()
# n1 = Node(1)
# tree.root = n1
n = int(input())
arr = [[] for _ in range(n+1)]
visited = [False] * (n+1)
answer = [0] * (n+1)

for i in range(n-1):
    n1, n2 = map(int, input().split())
    arr[n1].append(n2)
    arr[n2].append(n1)

def dfs(E,v,visited):
    visited[v]=True
    for i in E[v]:
        if not visited[i]:
            answer[i]=v
            print(answer)
            dfs(E, i, visited)
            

dfs(arr,1,visited)

for i in range(2,n+1):
    print(answer[i])
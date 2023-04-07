import sys
sys.setrecursionlimit(10**6)

def dfs(start,value):
    if distance[start] == -1:
        distance[start] =value
        for node,dis in graph[start]:
            dfs(node,value+dis)

n = int(input())
graph = {i:[] for i in range(1,n+1)}
for i in range(n-1):
    start,end,value = map(int,input().split())
    graph[start].append((end,value))
    graph[end].append((start,value))

distance = [-1] * (n+1)
dfs(1,0)
tmp_dis = -1
start=1
for idx,value in enumerate(distance):
    if tmp_dis < value:
        tmp_dis = value
        start = idx
distance = [-1] * (n+1)
dfs(start,0)
print(max(distance))
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

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
            dfs(E, i, visited) #노드를 탐색하기 직전의 노드를 부모로 기록
            

dfs(arr,1,visited)

for i in range(2,n+1):
    print(answer[i])
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(node):
    visited[node] = True
    dp[node][0] = 1
    for child_node in friend[node]: #자식노드 탐방
        if not visited[child_node]:
            dfs(child_node)
            dp[node][0] += min(dp[child_node][1], dp[child_node][0])
            dp[node][1] += dp[child_node][0]


n = int(input())
friend = [[] for i in range(n+1)]
dp = [[0,0] for i in range(n+1)] #dp[node][0] : node가 업리어답터일 때 최솟값, dp[node][1]: node가 업리어답터가 아닐 때 최솟값
visited = [False for _ in range(n+1)]

for i in range(n-1):
    u, v = map(int, input().split())
    friend[u].append(v)
    friend[v].append(u)
dfs(1)
print(min(dp[1][0], dp[1][1]))


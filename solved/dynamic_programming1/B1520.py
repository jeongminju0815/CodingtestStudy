#15:26
from collections import deque

#dp로 갈 수  있는 길  체크, dfs로 길 몇갠지 세기
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0 for i in range(m)] for _ in range(n)]
print(arr)
print(dp)
visited = [[False for i in range(len(arr[0]))] for _ in range(len(arr))]

for row in range(n):
    for col in range(m):
        if 



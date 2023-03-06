n,m = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(n)]

prefix_sum = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        prefix_sum[i][j] = arr[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

k = int(input())
for i in range(k):
    d = list(map(int,input().split()))
    print(prefix_sum[d[2]][d[3]] - prefix_sum[d[0]-1][d[3]] - prefix_sum[d[2]][d[1]-1] + prefix_sum[d[0]-1][d[1]-1])


    


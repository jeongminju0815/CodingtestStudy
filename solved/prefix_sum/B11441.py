n = int(input())
arr = list(map(int, input().split()))
m = int(input())
prefix_sum = [0] * (n+1)

for i in range(1,n+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

for i in range(m):
    s, e = map(int,input().split())
    print(prefix_sum[e] - prefix_sum[s-1])

    

n = int(input())
arr = list(map(int, input().split()))
inc_dp = [1] * (n)
dec_dp = [1] * (n)
max_length = 0

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            if inc_dp[i] < inc_dp[j]+1:
                inc_dp[i] = inc_dp[j] + 1

for i in range(n-1,-1,-1):
    for j in range(i, n):
        if arr[i] > arr[j]:
            if dec_dp[i] < dec_dp[j] + 1:
                dec_dp[i] = dec_dp[j] + 1

for i in range(n):
    total = inc_dp[i] + dec_dp[i] - 1
    if max_length < total:
        max_length = total
print(max_length)


        

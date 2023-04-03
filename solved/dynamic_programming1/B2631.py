n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [1] * n #자기 자신을 포함하는 경우 때문에 1로 초기화

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j]+1, dp[i])
print(n-max(dp)) #max(dp) 가 가장 긴 증가하는 부분 수열의 값 -> 이동하지 않아도 되는 값
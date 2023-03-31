n, k = map(int, input().split())
coin = []

for i in range(n):
    coin.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1

for i in range(len(coin)):
    c = coin[i]
    for j in range(c, k+1):
        dp[j] = dp[j-c] + dp[j]
print(dp[-1])
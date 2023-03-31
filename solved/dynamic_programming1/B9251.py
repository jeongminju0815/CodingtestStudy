s1 = input()
s2 = input()

dp = [[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]

for i in range(1,len(s2)+1):
    for j in range(1,len(s1)+1):
        if s2[i-1] == s1[j-1]: #문자가 같을때
            dp[i][j] = dp[i-1][j-1] + 1 #문자가 추가되기 전으로 가서 더해줌
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) #앞의 문자(j-1)가 업데이트 됐을 때를 고려해야 함, 이전 값과 비교

print(dp[len(s2)][len(s1)])


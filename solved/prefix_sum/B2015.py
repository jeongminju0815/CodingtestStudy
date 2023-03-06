from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

sum_num = n*(n+1)/2
prefix_sum = [0] * (n+1)
count = 0

for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

answer = 0
idx_dict = defaultdict(list)
print(prefix_sum)
for i in range(n,0,-1):
    SUM = prefix_sum[i]
    
    if SUM == k:
        answer+=1

    target = SUM+k
    # s[i] - s[i-1] = k, s[i] = s[i-1] + k 이용
    answer += len(idx_dict[target]) 
    
    idx_dict[SUM].append(i)
    
print(answer)
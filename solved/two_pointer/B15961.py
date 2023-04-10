from collections import defaultdict
import sys
input = sys.stdin.readline

n, d, k, c = map(int,input().split())
dish = []
for i in range(n):
    dish.append(int(input()))
dish.extend(dish)
right = 0
left = 0
susi = defaultdict(int)
susi[c] += 1
result = 0

for i in range(k):
    susi[dish[right]] += 1
    right += 1

while right < len(dish):
    result = max(result, len(susi))

    if susi[dish[left]] == 1:
        del susi[dish[left]]
    else:
        susi[dish[left]] -= 1
    left+=1
    susi[dish[right]] += 1
    right +=1
print(result)
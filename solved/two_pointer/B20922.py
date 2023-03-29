from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))
counter =defaultdict(int) #원소가 몇개 나왔는지 확인하는 dict
max_length = 0
right, left = 0, 0

while right < n:
    if counter[arr[right]] < k:
        counter[arr[right]]+=1
        right+=1
    else:
        counter[arr[left]] -= 1
        left +=1
    if max_length < right-left:
        max_length = right-left
print(max_length)
        
        
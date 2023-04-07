n, s = map(int,input().split())
arr = list(map(int,input().split()))
prefix_sum = [0] * (n+1)
length = 100000

for i in range(1,n+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

#누적합에서 투포인터를 이용하여 해당 구간합이 s보다 크면 s_p 앞으로 이동 작으면 e_p 앞으로 이동, 계속 min length 체크
right = 0
left = 0
length = 100001
total = 0

while True:
    if total < s:
        right += 1
        if right > n:
            break
    elif total >= s:
        length = min(right-left, length)
        left += 1
    if right == left:
        right += 1
        if right>n:
            break
    total = prefix_sum[right] - prefix_sum[left]

if length == 100001:
    print(0)
else:
    print(length)
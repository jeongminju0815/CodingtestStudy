import heapq

n = int(input())
coupon = list(map(int, input().split()))
arr = list(map(int, input().split()))
days = []

for i in range(n):
    days.append((coupon[i], arr[i]))

heapq.heapify(days)
arr.sort()
count = 0

while days:
    c, d = heapq.heappop(days)
    if c < d:
        plus = (d-c)//30 + 1
        count += plus
        heapq.heappush(days, (c + 30 * plus, d))

print(count)
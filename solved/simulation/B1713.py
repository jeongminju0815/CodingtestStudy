from collections import deque
import heapq
import sys

input = sys.stdin.readline

n = int(input())
recom = int(input())
check = [False] * (recom+1)
heap = [(0,1001, i) for i in range(recom+1)]
heap2 = [(0,1001, i) for i in range(recom+1)]
count = 0
old = 0

student = list(map(int, input().split()))

for s in student:
    if check[s]:
        value, o, idx = heap[s]
        heap[s] = (value+1, o, idx)
        continue
    if count >= n:
        idx = heapq.heappop(heap2)[2]
        check[idx] = False

        value, _, idx = heap[idx]
        heap[idx] = (value-1, 10001, idx)
        count-=1
    value, o, idx = heap[s]
    heap[s] = (value+1, old+1, idx)
    old+=1
    # heapq.heappush(heap2, (value+1, old,idx))
    heapq.heapify(heap2)
    check[s] = True
    count+=1
    print(heap)
print(heap,heap2)
for i in range(len(check)):
    if check[i]:
        print(i, end=" ")

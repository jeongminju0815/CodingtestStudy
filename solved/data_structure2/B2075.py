import heapq

n = int(input())
heap = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in temp:
        if len(heap) < n:
            heapq.heappush(heap, j)
        else:
            if heap[0] < j:
                heapq.heappop(heap) #가장작은 원소 제거
                heapq.heappush(heap, j)
print(heap[0])
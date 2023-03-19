### point ###
# 두개씩 카드를 묶고 바로 다른 카드 묶음과 비교할 필요 없음, 가장 작은 두개의 조합을 계속 찾아 더해줘야 함.
import heapq
import sys
input = sys.stdin.readline

cards = []
result = 0

for i in range(int(input())):
    heapq.heappush(cards, int(input()))

if len(cards) == 1:
    print(0)
else:
    while len(cards) > 1:
        plus = heapq.heappop(cards) + heapq.heappop(cards)
        result += plus
        heapq.heappush(cards, plus)
    print(result)
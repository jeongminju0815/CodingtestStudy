from collections import defaultdict

n = int(input())
card = list(map(int, input().split()))
card_dict = defaultdict(int)

for c in card:
    card_dict[c] += 1

m = int(input())
check = list(map(int, input().split()))

for c in check:
    print(card_dict[c], end=" ")
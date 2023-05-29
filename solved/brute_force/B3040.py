from itertools import combinations

arr = []

for i in range(9):
    arr.append(int(input()))

for i in combinations(arr,7):
    if sum(i) == 100:
        temp = i
    
for i in temp:
    print(i)
from collections import defaultdict

arr = defaultdict(int)
total = 0

for i in range(3):
    num = int(input())
    arr[num] += 1
    total += num

if total == 180:
    if len(arr) == 2:
        print("Isosceles")
    if len(arr) == 3:
        print("Scalene")
    if arr[60] == 3:
        print("Equilateral")
else:
    print("Error")
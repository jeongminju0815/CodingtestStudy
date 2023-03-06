def gcd(x,y):
    while(y):
        x,y = y, x %y
    return x

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

result = [False] * (max(arr)+1)

total = 0
count = 0
for i in arr:
    if not result[i]:
        result[i] = gcd(x, i)
    if result[i] == 1:
        total+=i
        count+=1
print(total/count)





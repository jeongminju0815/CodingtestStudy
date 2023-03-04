n = int(input())
idx = 0
num = [i for i in range(1,n+1)]
data = list(map(int, input().split()))
result = []

tmp = data.pop(idx)
result.append(num.pop(idx))

# idx : data에 인덱스 위치(현재 위치), tmp: 전에 터뜨린 풍선에 적힌 숫자
while data:
    if tmp >0:
        idx = (idx + (tmp-1)) % len(data)
    else:
        idx = (idx + tmp) % len(data)
    tmp = data.pop(idx)
    result.append(num.pop(idx))

for i in result:
    print(i, end = " ")
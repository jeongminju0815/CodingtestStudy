n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)
h = (start + end) // 2

while start<=end: #start==end==mid까지만 탐색
    total = 0
    for i in range(n):
        if h < tree[i]:
            total += (tree[i] - h)
    if total < m:
        end = h -1 
    else:
        result = h
        start = h + 1
    h = (end + start) // 2
print(h)


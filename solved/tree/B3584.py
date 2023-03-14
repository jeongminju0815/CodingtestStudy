# def bfs(parents, arr, check,i):
#     if check[i]:
#         return
#     parents[i] = arr[0]
#     check[i] = True

#     for i in range(1, len(arr[i])):
#         bfs(parents, arr, check, i)

# def bfs(arr, )

testcase = int(input())

for t in range(testcase):
    n = int(input())
    parents = [0] * (n+1)
    check = [False] * (n+1)
    arr = [[] for _ in range(n+1)]
    for i in range(n-1):
        a, b = map(int, input().split())
        arr[b].append(a)
    
    print("구하기")
    a, b = map(int, input().split())
    print(arr)



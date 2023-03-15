from collections import deque
# def bfs(parents, arr, check,i):
#     if check[i]:
#         return
#     parents[i] = arr[0]
#     check[i] = True

#     for i in range(1, len(arr[i])):
#         bfs(parents, arr, check, i)

testcase = int(input())

def bfs(temp):
    q = deque([temp])
    while q:
        a, b = q.popleft()
        print(a,b)
        if len(arr[a]) == 1:
            print(a)
            break
        if len(arr[b]) == 1:
            print(b)
            break
        if arr[a][1] == arr[b][1]:
            print(arr[a][1])
        else:
            q.append([arr[a][1], arr[b][1]])

for t in range(testcase):
    n = int(input())
    parents = [0] * (n+1)
    check = [False] * (n+1)
    arr = [[0] for _ in range(n+1)]
    for i in range(n-1):
        a, b = map(int, input().split())
        arr[a][0] += 1
        arr[b].append(a)
    
    print("구하기")
    a, b = map(int, input().split())
    print(arr)
    bfs([a,b])



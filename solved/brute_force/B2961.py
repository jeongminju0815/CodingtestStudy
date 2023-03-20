# def check(temp):
#     sour = 1
#     bitter = 0
#     for i in temp:
#         sour *= arr[i][0]
#         bitter += arr[i][1]
#     return abs(sour-bitter)
        

# from itertools import combinations

# n = int(input())
# num = [i for i in range(n)]
# arr = []
# combi = []
# result = 1000000000

# for i in range(n):
#     arr.append(list(map(int, input().split())))

# for i in range(1, n+1):
#     for j in list(combinations(num, i)):
#         _result = check(j)
#         if _result < result:
#             result = _result

# print(result)

def dfs(depth, start):
    print(f"dfs========={depth}{start}")
    global result
    # 기저
    if depth == len_:  # 만약 깊이가 뽑을 개수와 같다면(len_개 만큼 뽑았다면)
        print("길이 일치!")
        lemon = 1  # 신맛
        bad = 0  # 쓴맛
        for i in arr:  # 뽑은 신맛 쓴맛을 계산한다.
            lemon *= i[0]  # 신맛 값들을 곱해준다.
            bad += i[1]  # 쓴맛 값들을 더해준다.
        if abs(bad - lemon) < result:  # 만약 그 차가 저장된 값보다 적다면
            result = abs(bad - lemon)  # 그 차를 결과에 저장
        return  # 그 후 재귀 종료
    # 재귀
    for i in range(start, N):
        arr.append(cuisine[i])
        print("arr : ", arr)
        print(f"start======dfs {depth+1}, {i+1}=====")
        dfs(depth + 1, i + 1)
        print(f"end======dfs {depth+1}, {i+1}=====")
        arr.pop()


N = int(input())
cuisine = [list(map(int, input().split())) for i in range(N)]
arr = []
result = 1 << 100  # 결과값을 처음에 아주 큰 값으로 초기화

for i in range(1, N + 1):  # 1~N 개까지 뽑아서 비교한다.
    len_ = i
    print("=====================반복문============")
    dfs(0, 0)

print(result)
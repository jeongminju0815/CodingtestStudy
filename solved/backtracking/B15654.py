s = []

def backtracking():
    if len(s) == m:
        print(" ".join(map(str, s)))
        return 
    for i in arr:
        if i not in s:
            s.append(i)
            backtracking()
            s.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
backtracking()
s =[0]
def backtrack(s, min_sum, total):
    if len(s) == n and arr[s[-1]][0]!=0:
        total += arr[s[-1]][0]
        if min_sum > total:
            min_sum = total
        return min_sum
    
    for i in range(1, n):
        if not i in s and arr[s[-1]][i]!=0:
            total += arr[s[-1]][i]
            s.append(i)
            min_sum = backtrack(s, min_sum, total)
            last = s.pop()
            total -= arr[s[-1]][last]
    return min_sum
n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]

print(backtrack(s, 1e9, 0))
t = int(input())

def factorial(n):
    f = 1
    for i in range(n):
        f *= (i+1)
    return f

for i in range(t):
    n,m = map(int, input().split())

    #mCn구현
    print(factorial(m)// (factorial(n) * factorial(m-n)))
    

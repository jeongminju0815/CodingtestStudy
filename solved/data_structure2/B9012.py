n = int(input())

for i in range(n):
    stack = []
    arr = input()
    flag = False

    for s in arr:
        if s == "(":
            stack.append("(")
        else:
            if len(stack) == 0:
                flag = True
                break
            stack.pop()

    if len(stack) > 0 or flag:
        print("NO")
    else:
        print("YES")
s = input().rstrip()
bomb = input().rstrip()
stack = []

for i in range(len(s)):
    stack.append(s[i])
    if stack[-1] == bomb[-1] and len(stack) >= len(bomb):
        if ''.join(stack[-len(bomb):]) == bomb:
            for j in range(len(bomb)):
                stack.pop()
if stack:
    print(''.join(stack))
else:
    print("FRULA")
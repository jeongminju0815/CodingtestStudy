strn = list(input())
stack=[]
res=''
for s in strn:
    if s.isalpha():
        res+=s
    else:
        print(stack)
        print("====")
        if s == '(':
            stack.append(s)
        elif s == '*' or s == '/':
            while stack and (stack[-1] == '*' or stack[-1] =='/'):
                res += stack.pop()
            stack.append(s)
        elif s == '+' or s == '-':
            while stack and stack[-1] != '(':
                res+= stack.pop()
            stack.append(s)
        elif s == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
        print(stack)
while stack :
    res+=stack.pop()
print(res)
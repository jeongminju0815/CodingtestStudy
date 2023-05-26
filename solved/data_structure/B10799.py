st = input()
stick = []
result = 0
bomb = False

for i in range(len(st)-1):
    if st[i] == "(":
        if st[i+1] == ")":
            bomb = True
        if st[i+1] == "(":
            stick.append("(")
            bomb = False
    else:
        if not bomb:
            stick.pop()
            result += 1
        else:
            result += len(stick)
            bomb = False

if len(stick) > 0:
    print(result + 1)
else:
    print(result) 
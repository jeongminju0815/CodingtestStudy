s = input()
s = s.split()
t = s[0]
stack = []

for i in range(1, len(s)):
    temp = t
    alpha = ""
    r = list(s[i])
    r.reverse()

    for j in r:
        if j == ",":
            continue
        if j.isalpha():
            alpha = j + alpha
        else:
            if j == ";":
                continue
            if j == "]":
                stack.append(j)
                continue
            if j =="[":
                temp += j
                temp += stack.pop()
                continue
            temp += j
    print(temp+" "+alpha+";")
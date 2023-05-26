from collections import defaultdict

s = input()
check = defaultdict(int)
flag = [False, False]

for i in s:
    if i == "0":
        if flag[1] == True:
            flag = [True, False]
            check[1] += 1
            continue
        flag[0] = True
    else:
        if flag[0] == True:
            flag = [False, True]
            check[0] += 1
            continue
        flag[1] = True
if len(check) == 0:
    print(0)
else:
    if flag[0]:
        check[0] += 1
    else:
        check[1] += 1
    print(min(check.values()))
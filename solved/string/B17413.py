s = input()
length = len(s)
result = "" #기호를 담기위해
sign_check = False #괄호 확인
sign = ""
word = ""


for i in range(len(s)):
    if sign_check:
        sign += s[i]
    if s[i] == ">":
        sign_check = False
        result += sign
        sign = ""
    elif s[i] == "<":
        if word != "":
            result+=word
            word = ""
        sign_check = True
        sign += s[i]
    elif s[i] == " ":
        if word !="":
            result += word + s[i]
            word = ""
    else:
        if sign_check:
            continue
        word = s[i]+word
if word !="":
    result += word 
    word = ""

print(result)
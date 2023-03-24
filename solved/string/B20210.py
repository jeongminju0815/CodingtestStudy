from collections import defaultdict

def dfs(files, depth, finish):
    score = defaultdict(list) #집단을 묶어주기 위해서
    # if len(files) == 1:
    #     result.append(files)
    # if finish:
    #     result.append()
    length = len(files)
    for i in length:
        score[files[i][depth]].append(files[i][depth:]) #score F:0,1,2,.. f:7

    for key, value in score.items():
        if key.isdigit():
            
        # dfs(value, depth+1, finish)


    



n = int(input())
files = []
result = []
alphabet = {"A":0,"a":1,"B":2,"b":3,"C":4,"c":5,"D":6,"d":7,"E":8,"e":9,"F":10,"f":11,"G":12,"g":13,"H":14
,"h":15,"I":16,"i":17,"J":18,"j":19,"K":20,"k":21,"L":22,"l":23,"M":24,"m":25,"N":26,"n":27,"O":28,"o":29,
"P":30,'p':31,"Q":32,"q":33,"R":34,"r":35,"S":36,"s":37,"T":38,"t":40,"X":41,"x":42,"Y":43,"y":44,"Z":45,"z":46}
# 숫자, 대문자, 소문자 우선순위를 구분하는 지표가 있어야 함.
# 자리 수별로 비교하려 했는데 숫자가 계속 나온다면..

check = [False] * n
shortest = 101
for i in range(n):
    temp = input()
    files.append(temp)
    if len(temp) < shortest:
        shortest = len(temp)


finish = False
dfs(files, 0, finish, shortest) #비교할 대상 ,깊이

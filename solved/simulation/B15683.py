from collections import defaultdict
from itertools import combinations,product

n,m = map(int, input().split())
arr = []
point = {1: [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)], 
2:[(1,1,0,0), (0,0,1,1)], 
3:[(1,0,1,0),(0,1,0,1),(1,0,0,1),(0,0,1,1)], 
4:[(1,1,1,0),(0,1,1,1),(1,0,1,1),(1,1,0,1)], 
5:[(1,1,1,1)]} #[상,하,좌,우]

check = [[False for i in range(m)] for j in range(n)]
located = defaultdict(list)
move = defaultdict(int)
count = []
cctv_num = 0
box = 0 #사각지대

for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
    for j in range(len(temp)):
        if temp[j]!=0:
            located[temp[j]].append((i,j)) #행,열
            if temp[j] != 6:
                length = [(temp[j],k) for k in range(len(point[temp[j]]))]
                count.append(length)
                cctv_num += 1
        else:
            box +=1 

print(located,count)
combi = list(product(*count))
print(combi)
for c in combi:
    check = [[False for i in range(m)] for j in range(n)] #행열 범위안에 있는지 확인
    cctv_list = []
    box_copy = box.copy()
    for i in range(len(c)): #위치가 필요한 이유: located에 접근하기 위해
        cctv = c[i][0] #cctv 유형
        ro = c[i][1] #회전 방향
        up_flag = False
        down_flag = False
        right_flag = False
        left_flag = False
        row, col = located[cctv][move[cctv]] #해당 위치
        move[cctv]+=1

        #벽이 있는지
        for wall_row, wall_col in located[6]:
            if (row==wall_row):
                if wall_row > row:
                    down_flag= True
                else:
                    up_flag= True
            if (col==wall_col):
                if wall_col > row:
                    right_flag= True
                else:
                    left_flag= True
        #사각지대 빼주기
        #상
        if point[cctv][ro][0] == 1:
            if up_flag:
                box_copy -= abs(row - wall_row)
            else:
                box_copy -= row
            
        #하
        if point[cctv][ro][1] == 1:
            if down_flag:
                box_copy -= abs(wall_row - row)
            else:
                box_copy -= n-row-1
        #좌
        if point[cctv][ro][2] == 1:
            if right_flag:
                box_copy -= abs(wall_col - col)
            else:
                box_copy -= m-col-1
        #우
        if point[cctv][ro][3] == 1:
            if left_flag:
                box_copy -= abs(wall_col - col)
            else:
                box_copy -= col
        
        
















    




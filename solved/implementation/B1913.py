def add_idx(odd, before): #바퀴수, 시작할 숫자, 기록할 리스트
    global result, result_matrix

    before_row, before_col = result[before]
    start_row = before_row-1
    start_col = before_col -1
    
    start = odd **2
    for row in range(odd):
        result[start] = [start_row+row, start_col]
        result_matrix[start_row+row][start_col] = start
        start-=1

    for col in range(1,odd):
        result[start] = [start_row+row, start_col+col]
        result_matrix[start_row+row][start_col+col] = start
        start-=1

    for row2 in range(row-1, 0, -1):
        result[start] = [start_row+row2, start_col+col]
        result_matrix[start_row+row2][start_col+col] = start
        start-=1

    for col in range(odd-1,0,-1):
        result[start] = [start_row, start_col+col]
        result_matrix[start_row][start_col+col] = start
        start-=1

from collections import defaultdict

n = int(input())
m = int(input())

odd = 1
start = n//2
start_row = start
start_col = start
result = defaultdict(list) #1~n까지 위치 저장
result[1] = [start_row, start_col]
result_matrix= [[0 for i in range(n)] for _ in range(n)]
result_matrix[start_row][start_col] = 1

start_idx = 3

for i in range(start): #1을 제외한 바퀴 수
    before = odd**2
    odd +=2
    add_idx(odd, before)
            
for i in range(n):
    for j in range(n):
        print(result_matrix[i][j], end=" ")
    print()            

print(result[m][0]+1, result[m][1]+1)




    

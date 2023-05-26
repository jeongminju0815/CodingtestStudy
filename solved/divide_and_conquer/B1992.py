def divide(m, row, col):
    if m == 1:
        result.append(arr[row][col])
        return

    temp = arr[row][col]

    for i in range(row, row+m):
        for j in range(col, col+m):
            if arr[i][j] == temp:
                visited[i][j] = True
            if arr[i][j] != temp and not visited[i][j]:
                result.append("(")
                divide(m//2, row, col)
                divide(m//2, row, col + m//2)
                divide(m//2, row + m//2, col)
                divide(m//2, row + m//2, col + m//2)
                result.append(")")
                return
            
    result.append(temp)

m = int(input())
arr = []
visited = [[False]*m for i in range(m)]
for i in range(m):
    arr.append(input())

result = []
divide(m, 0, 0)
print("".join(result))
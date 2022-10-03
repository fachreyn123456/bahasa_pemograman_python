MatA = [
    [4, 2],
    [3, 3],
]
MatB = [
    [2, 3],
    [1, 5],
]
for x in range(0, len(MatA)):
    for y in range(0, len(MatA[0])):
        print (MatA[x][y] + MatB[x][y], end= ' '),
        print ()
        

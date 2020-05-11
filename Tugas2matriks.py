#>>(penjumlahan matriks)<<

mat1 = [
    [1, 2],
    [1, 2],
]

mat2 = [
    [3, 3],
    [3, 3],
]

for x in range(0, len(mat1)):
    for y in range(0, len(mat1[0])):
        print (mat1[x][y] + mat2[x][y], end=' '),
    print()
	
#>>(perkalian matriks)<<

mat1 = [
    [1, 2],
    [1, 2],
]

mat2 = [
    [3, 3],
    [3, 3],
]

mat3 = []

for x in range(0, len(mat1)):
    row = []
    for y in range(0, len(mat1[0])):
        total = 0
        for z in range(0, len(mat1)):
            total = total + (mat1[x][z] * mat2[z][y])
        row.append(total)
    mat3.append(row)

for x in range(0, len(mat3)):
    for y in range(0, len(mat3[0])):
        print (mat3[x][y], end=' ')
    print ()
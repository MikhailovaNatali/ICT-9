size1 = int(input())
size2 = int(input())
size3 = int(input())
matrix1 = [[0 for _ in range(size1)] for _ in range(size2)]
matrix2 = [[0 for _ in range(size2)] for _ in range(size3)]
matrix = [[0 for _ in range(size1)] for _ in range(size3)]
for i in range(0, size2):
	for j in range(0, size1):
		matrix1[i][j] = int(input())
print (matrix1)
for i in range(0, size3):
	for j in range(0, size2):
		matrix2[i][j] = int(input())
print (matrix2)
for i in range(0, size1):
	for j in range(0, size3):
		for r in range(0, size2):
			matrix[i][j] += (matrix1[i][r]*matrix2[r][j])
print(matrix)

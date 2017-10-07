matrix = []
with open('p081_matrix.txt')as m:
	mat = m.read().split("\n")

for i in mat:
	lst = i.split(",")
	matrix.append(lst)
matrix.pop()

summ = 0
size = 80
for i in range(78,-1,-1):
	matrix[79][i] = str(int(matrix[79][i]) + int(matrix[79][i+1]))
	matrix[i][79] = str(int(matrix[i][79]) + int(matrix[i+1][79]))

for i in range(78,-1,-1):
	for j in range(78,-1,-1):
		matrix[i][j] = str(int(matrix[i][j]) + min(int(matrix[i+1][j]),int(matrix[i][j+1])))
print(matrix[0][0])

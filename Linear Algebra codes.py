# Vector 의 계산

u = [2,2]
v = [2,3]
z = [3,5]

result = []

for i in range(len(u)):
    result.append(u[i] + v[i] + z[i])

print(result)

# 파이썬 답지 못하고 아름답지 않다

# zip을 이용해 깔끔하게 계산

result = [sum(t) for t in zip(u,v,z)]
print(result)

# Vector의 계산 : Scala-Vector product

u = [1,2,3]
v = [4,4,4]
alpha = 2

result = [alpha*sum(t) for t in zip(u,v)]
print(result)

# Matrix representation of python

matrix_a = [[3,6],[4,5]] # List
matrix_b = [(3,6),(4,5)] # Tuple
matrix_c = {(0, 0) : 3, (0,1) : 6, (1,0) : 4, (1,1) : 5} # Dict

print(matrix_a, matrix_b, matrix_c)

# Matrix 의 계산 : Matrix addition

matrix_a = [[3,6], [4,5]]
matrix_b = [[5,8], [6,7]]
result = [[sum(row) for row in zip(*t)] for t in zip(matrix_a,matrix_b)]
print(result)

# Matrix 의 계산 : Matrix Transpose

matrix_a = [[1,2,3],[4,5,6]]
result = [[element for element in t] for t in zip(*matrix_a)]
print(result)

# Matrix 의 계산 : Matrix Product

matrix_a = [[1,1,2], [2,1,1]]
matrix_b = [[1,1,],[2,1],[1,3]]
result = [[sum(a*b for a,b in zip(row_a,column_b))\
    for column_b in zip(*matrix_b)]for row_a in matrix_a]

print(result)
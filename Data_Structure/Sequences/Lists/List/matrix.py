print("------------------------------------------------------------------1----")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2]) 
print("------------------------------------------------------------------2----")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

for row in transposed:
    print(row)
print("------------------------------------------------------------------3----")
#Меняет строки и столбцы местами (поворачивает матрицу).
import numpy as np
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(matrix.T) 
print("------------------------------------------------------------------4----")
# Перемножает две 2×2 матрицы.
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

for row in result:
    print(row)
print("------------------------------------------------------------------5----")
 #Создаёт матрицу 3×4, заполняя её числами по порядку, и выводит на экран.
rows, cols = 3, 4
matrix = [[(i * cols) + j + 1 for j in range(cols)] for i in range(rows)]

for row in matrix:
    print(row)
print("------------------------------------------------------------------6----")
#Перемножает две 2×2 матрицы.
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

for row in result:
    print(row)
print("------------------------------------------------------------------7---")
#просто создаём случайную матрицу 5×5 со случайными цифрами, находим и выводим её максимальный элемент.
import random

matrix = [[random.randint(1, 100) for _ in range(5)] for _ in range(5)]
max_value = max(max(row) for row in matrix)

for row in matrix:
    print(row)
print("Максимальный элемент:", max_value)
print("------------------------------------------------------------------8----")

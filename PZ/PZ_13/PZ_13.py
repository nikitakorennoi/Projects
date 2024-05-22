'''1. В матрице найти сумму и произведение элементов столбца N (N задать с
клавиатуры).'''
import random

n = int(input('Введите количество столбцов матрицы: '))
m = int(input('Введите количество строк матрицы: '))

matrix = [[random.randrange(-10, 10) for i in range(n)] for j in range(m)]
for row in matrix:
    print(row)

N = int(input('Введите номер столбца (от 0 до {}): '.format(n - 1)))

# Сумма
sum_ = sum(matrix[i][N] for i in range(m))
print('Сумма элементов столбца {}: {}'.format(N, sum_))

# Произведение
column_ = 1
for i in range(m):
    column_ *= matrix[i][N]
print('Произведение элементов столбца {}: {}'.format(N, column_))

'''2. В матрице найти отрицательные элементы, сформировать из них новый массив.
Вывести размер полученного массива.'''

negative_elements = [element for row in matrix for element in row if element < 0]

print('Отрицательные элементы в матрице:', negative_elements)
print('Размер полученного массива:', len(negative_elements))

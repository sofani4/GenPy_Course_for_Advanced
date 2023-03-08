# 4.5.1 Таблица умножения
n, m = int(input()), int(input())

for i in range(n):
    for j in range(m):
        print(str((i * j)).ljust(2), end=' ')
    print()

# 4.5.2 Максимум в таблице
# вывести два числа: номер строки и номер столбца, в которых стоит наибольший элемент таблицы.
n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
row = col = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] > matrix[row][col]:
            row, col = i, j
print(row, col)


# 4.5.3 Обмен столбцов
# Формат входных данных
# На вход программе на разных строках подаются два натуральных числа
# n и m — количество строк и столбцов в матрице, затем элементы матрицы построчно
# через пробел, затем числа ii и jj — номера столбцов, подлежащих обмену.
n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
col1, col2 = [int(i) for i in input().split()]
for i in range(n):
    matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]
    print(*matrix[i])

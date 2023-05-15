# 5.1.1 Каждый n-ый элемент
# Sample Input 1:
# a b c d e f g h i j k l m n
# 3
# Sample Output 1:
# [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

str = input().split()
n = int(input())
lst = []

for i in range(n):
    lst.append(str[i::n])
print(lst)

# 5.1.2 Максимальный в области 2
# Напишите программу, которая выводит максимальный элемент
# в нижней части побочной диагонали (включая значения побочной диагонали)

n = int(input())
matrix = [input().split() for _ in range(n)]
max_n = matrix[0][0]
for i in range(n):
    for j in range(n):
        if i >= n - 1 - j:
            if max_n < matrix[i][j]:
                max_n = matrix[i][j]
print(max_n)

# 5.1.3 Транспонирование матрицы
n = int(input())
matrix = [input().split() for _ in range(n)]
for i in range(n):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()

# 5.1.4 Снежинка
n = int(input())
for i in range(n):
    for j in range(n):
        if i == j or i == n - 1 - j or i == n // 2 or j == n // 2:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()

# 5.1.5 Симметричная матрица
# Напишите программу проверки симметричности квадратной матрицы относительно побочной диагонали.
# Программа должна вывести YES, если матрица симметрична, и слово NO в противном случае.
def check_symmetry(matrix, n):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[n - j - 1][n - i - 1]:
                return 'NO'
    return 'YES'

n = int(input())
matrix = [input().split() for _ in range(n)]
print(check_symmetry(matrix, n))

# 4.5.7 Поворот матрицы
# Напишите программу, которая поворачивает квадратную матрицу чисел на 90∘ по часовой стрелке.
# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.
# Формат выходных данных
# Программа должна вывести результат на экран, числа должны быть разделены одним пробелом.

def rotation_90(matrix, n):
    for i in range(n):
        for j in range(n - 1, -1, -1):
            print(matrix[j][i], end=' ')
        print()


# Если нужно создать повернутую матрицу, а не просто вывести
def rotation_90_v2(matrix, n):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = matrix[n - j - 1][i]
    for row in result:
        print(*row)


n = int(input())
matrix = [input().split() for _ in range(n)]

rotation_90(matrix, n)
# rotation_90_v2(matrix, n)

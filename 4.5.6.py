# 4.5.6 Зеркальное отображение
# Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы относительно
# горизонтальной оси симметрии.


def mirroring1(matrix, n):  # v1
    for i in range(n // 2):
        matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
    for row in matrix:
        print(*row)


def mirroring2(matrix):  # v2
    matrix = matrix[::-1]
    for row in matrix:
        print(*row)


def mirroring3(matrix, n):  # v3
    for row in range(n - 1, -1, -1):
        print(*matrix[row])


n = int(input())
matrix = [input().split() for _ in range(n)]
# mirroring1(matrix, n)
#mirroring2(matrix)
mirroring3(matrix, n)

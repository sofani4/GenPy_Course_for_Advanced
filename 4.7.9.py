# 4.7.9 Сложение матриц
# Напишите программу для вычисления суммы двух матриц.
n, m = map(int, input().split())

matrix1 = [[int(i) for i in input().split()] for _ in range(n)]
input()
matrix2 = [[int(i) for i in input().split()] for _ in range(n)]
matrix3 = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix3[i][j] += matrix1[i][j] + matrix2[i][j]

[print(*i) for i in matrix3]


# 4.6.5 Заполнение 3
# Sample Input 2:
# 4
# Sample Output 2:
# 1  0  0  1
# 0  1  1  0
# 0  1  1  0
# 1  0  0  1


def filling_3(n):
    for i in range(n):
        for j in range(n):
            print(1 if i == j or n - i - 1 == j else 0, end=' ')
        print()

# filling_3(int(input()))
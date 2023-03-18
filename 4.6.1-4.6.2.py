# 4.6.1 Шахматная доска
#  Sample Input 1:
# 3 4
# Sample Output 1:
# . * . *
# * . * .
# . * . *

# v1 без сохранения матрицы
def сhessboard(n, m):
    for i in range(n):
        for j in range(m):
            if (i + j) % 2 == 0:
                print('.', end=' ')
            else:
                print('*', end=' ')
        print()


# v2 без сохранения матрицы
def сhessboard2(n, m):
    for i in range(n):
        for j in range(m):
            print('.*'[(i + j) % 2], end=' ')
            print()


# v3 с сохранением матрицы
def сhessboard3(n, m):
    board = [['.'] * m for _ in range(n)]

    for i in range(n):
        for j in range(1 - i % 2, m, 2):
            board[i][j] = '*'

    for row in board:
        print(*row)


# n, m = [int(i) for i in input().split()]
# сhessboard2(n, m)
# сhessboard3(n, m)


# 4.6.2 Побочная диагональ
# Sample Input 1:
# 4
# Sample Output 1:
# 0 0 0 1
# 0 0 1 2
# 0 1 2 2
def side_diagonal(n):
    for i in range(n):
        for j in range(n):
            if n - 1 - i == j:
                print(1, end=' ')
            elif i >= j and i < n - 1 - j or i < j and i < n - 1 - j:
                print(0, end=' ')
            else:
                print(2, end=' ')
        print()


# side_diagonal(int(input()))

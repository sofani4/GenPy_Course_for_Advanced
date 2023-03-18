# 4.6.6 Заполнение 4
# 4
# 1  1  1  1
# 0  1  1  0
# 0  1  1  0
# 1  1  1  1

def filling_4(n):
    for i in range(n):
        for j in range(n):
            print(1 if (i <= j and i <= n - 1 - j) or
                       (i >= j and i >= n - 1 - j) else 0, end=' ')
        print()


# filling_4(int(input()))

# 4.6.7 Заполнение 5 🌶️
#  Sample Input 3:
# 3 7
# Sample Output 3:
# 1 2 3 4 5 6 7
# 2 3 4 5 6 7 1
# 3 4 5 6 7 1 2

def filling_5(n, m):
    matrix = [*range(1, m + 1)]
    for i in range(n):
        print(*matrix)
        matrix.append(matrix.pop(0))


# n, m = [int(i) for i in input().split()]
# filling_5(n, m)

# 4.6.8 Заполнение змейкой
# Sample Input 1:
# 3 5
# Sample Output 1:
# 1  2  3  4  5
# 10 9  8  7  6
# 11 12 13 14 15


def snake(n, m):
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 1
    for i in range(n):
        for j in range(m):
            if i % 2 == 0:
                matrix[i][j] = cnt
                cnt += 1
            else:
                matrix[i][m - 1 - j] = cnt
                cnt += 1

    # [print(*i) for i in matrix] # без ljust
    # с учетом ljust
    for row in matrix:
        for el in row:
            print(f'{el:<3}', end=' ')
        print()


# n, m = [int(i) for i in input().split()]
# snake(n, m)

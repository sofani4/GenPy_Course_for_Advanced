# 4.6.3 Заполнение 1
# Sample Input 1:
# 3 4
# Sample Output 1:
# 1  2  3  4
# 5  6  7  8
# 9  10 11 12

def filling_1(n, m):
    cnt = 1
    for i in range(n):
        for j in range(m):
            print(f'{cnt}'.ljust(2), end=' ')
            cnt += 1
        print()


# n, m = [int(i) for i in input().split()]
# filling_1(n, m)

# 4.6.4 Заполнение 2
#  Sample Input 1:
# 3 7
# Sample Output 1:
# 1  4  7  10 13 16 19
# 2  5  8  11 14 17 20
# 3  6  9  12 15 18 21

def filling_2(n, m):
    matrix = [[0 for i in range(m)] for _ in range(n)]
    cnt = 1
    for i in range(m):
        for j in range(n):
            matrix[j][i] += cnt
            cnt += 1

    [print(*row) for row in matrix]


# n, m = [int(i) for i in input().split()]
# filling_2(n, m)

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
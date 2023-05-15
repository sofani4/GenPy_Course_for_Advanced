# 5.1.6 Латинский квадрат 🌶️
# Латинским квадратом порядка nn называется квадратная матрица размером n×n,
# каждая строка и каждый столбец которой содержат все числа от 1 до n.
# Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским квадратом.
# Sample Input 1:
# 4
# 2 3 4 1
# 3 4 1 2
# 4 1 2 3
# 1 2 3 4
# Sample Output 1:
# YES

n = int(input())
matrix = [input().split() for _ in range(n)]
matrix_t = list(zip(*matrix))
set_m = set(str(i) for i in range(1, n + 1))

flag = 1
for i in range(n):
    if set_m != set(matrix[i]) or set_m != set(matrix_t[i]):
        flag = 0
        break

print('YES' if flag else 'NO')

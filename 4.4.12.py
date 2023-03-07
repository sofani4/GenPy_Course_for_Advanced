# 4.4.12 Максимальный в области 1
n = int(input())
lst = [[int(i) for i in input().split()] for _ in range(n)]
max_int = lst[0][0]

for i in range(n):
    for j in range(i+1):
        if max_int < lst[i][j]:
            max_int = lst[i][j]
print(max_int)


# 4.4.13 Максимальный в области 2 🌶️
# Напишите программу, которая выводит максимальный элемент в
# заштрихованной области квадратной матрицы.

n = int(input())
lst = [[int(i) for i in input().split()] for _ in range(n)]
max_int = lst[0][0]

for i in range(n):
    for j in range(n):
        if (i >= j and i <= n - 1 - j) or (i <= j and i >= n - 1 - j):
            if max_int < lst[i][j]:
                max_int = lst[i][j]
print(max_int)


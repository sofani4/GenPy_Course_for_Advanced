# Вывести матрицу 1
# Формат входных данных
# На вход программе подаются два числа nn и mm — количество строк и столбцов в матрице,
# далее идут n×mn×m слов, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести считанную матрицу, разделяя ее элементы одним пробелом.
# v1
n, m = int(input()), int(input())
for i in range(n):
    tmp = []
    for j in range(m):
        tmp.append(input())
    print(" ".join(tmp))

# v2
n, m = int(input()), int(input())
for i in range(n):
    for j in range(m):
        print(input(), end=' ')
    print()

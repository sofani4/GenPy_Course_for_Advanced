# 4.3.10 Треугольник Паскаля 1 🌶️
# Формат входных данных
# На вход программе подается число n (n≥0).
# Формат выходных данных
# Программа должна вывести указанную строку треугольника Паскаля в виде списка.


# Треугольник Паскаля 2
def pascal(n):
    lst = []
    for i in range(n + 1):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if j != i and j != 0:
                row[j] = lst[i - 1][j - 1] + lst[i - 1][j]
        lst.append(row)
    return print([1] if n == 0 else lst[n])


pascal(int(input()))

# 4.3.11 Треугольник Паскаля 2
# Формат входных данных
# На вход программе подается число n (n≥1).
#
# Формат выходных данных
# Программа должна вывести первые nn строк треугольника Паскаля,
# каждую на отдельной строке в соответствии с образцом.
def pascal2(n):
    lst = []
    for i in range(n + 1):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if j != i and j != 0:
                row[j] = lst[i - 1][j - 1] + lst[i - 1][j]
        lst.append(row)
    for i in range(len(lst) - 1):
        print(*lst[i])


pascal2(int(input()))

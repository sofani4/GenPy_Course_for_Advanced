# Магический квадрат 🌶️
# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы: nn строк, по nn чисел в каждой, разделённые пробелами.
#
# Формат выходных данных
# Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.'
# МГ - суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой


def check_magic_square(matrix, n):
    sum_compare = sum0 = sum1 = sum2 = 0
    n_sqr = n ** 2
    set_num = set()
    # цикл для диагоналей
    for i in range(n):
        elem1 = matrix[i][i]
        elem2 = matrix[i][n - i - 1]
        if 0 < elem1 <= n_sqr and 0 < elem2 <= n_sqr:
            set_num.update({elem1, elem2})
        else:
            return 'NO'
        sum_compare += elem1  # сумма главной диагонали
        sum0 += elem2  # сумма побочной диагонали
    if sum_compare != sum0:
        return 'NO'

    for i in range(n):
        for j in range(n):
            elem1 = matrix[i][j]
            elem2 = matrix[j][i]
            if 0 < elem1 <= n_sqr and 0 < elem2 <= n_sqr:
                set_num.update({elem1, elem2})
            else:
                return 'NO'
            sum1 += elem1  # сумма по горизонтали
            sum2 += elem2  # сумма по вертикали
        if sum_compare != sum1 or sum_compare != sum2:
            return 'NO'
        sum1 = sum2 = 0
    return 'YES' if len(set_num) == n ** 2 else 'NO'


n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
print(check_magic_square(matrix, n))

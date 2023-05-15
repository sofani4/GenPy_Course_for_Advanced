# 4.6.9 Заполнение диагоналями 🌶️
# Sample Input 2:
# 3 4
# Sample Output 2:
# 1  2  4  7
# 3  5  8  10
# 6  9  11 12

def filling_with_diagonals(n, m):
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    nmb = 1
    for i in range(n + m):
        for j in range(n):
            for c in range(m):
                if j == i - c - 1:
                    matrix[j][c] = nmb
                    nmb += 1
                # break, чтоб было меньше итераций
                if j > i - c - 1:
                    break

    for row in matrix:
        for el in row:
            print(f'{el:<3}', end=' ') # f'{el:<3}' - форматирование вывода - 3 символа
        print()


n, m = map(int, input().split())
filling_with_diagonals(n, m)

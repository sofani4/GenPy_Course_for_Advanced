# Ходы коня
# col, row = input().strip()
# coor_col = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
# coor_row = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
# arr = [['N' if [i, j] == [coor_row[row], coor_col[col]] else '.' for j in range(8)] for i in range(8)]
# for i in range(8):
#     for j in range(8):
#         if (coor_row[row] - i) * (coor_col[col] - j) in [-2, 2]: arr[i][j] = '*'
# for line in arr:
#     print(*line, sep = ' ')


rows = ['8', '7', '6', '5', '4', '3', '2', '1']
cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
matrix = [['.'] * 8 for _ in range(8)]
col, row = input().strip()
matrix[rows.index(row)][cols.index(col)] = 'N'

for i in range(8):
    for j in range(8):
        if (rows.index(row) - i) * (cols.index(col) - j) in [-2, 2]:
            matrix[i][j] = '*'

for line in matrix:
    print(*line, sep=' ')


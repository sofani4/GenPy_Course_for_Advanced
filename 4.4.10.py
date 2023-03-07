# След матрицы
# v1
n = int(input())
matrix = []
sum = 0

for i in range(n):
    matrix.append(input().split())

for i in range(n):
    sum += int(matrix[i][i])

print(sum)

# v2 которая запись в list
n = int(input())
sum = 0
tmp = [list(input().split()) for _ in range(n)]
for i in range(n):
    sum += int(tmp[i][i])
print(sum)


# v3 без сохранения матрицы
sum = 0
for i in range(int(input())):
    sum += int(input().split()[i])
print(sum)
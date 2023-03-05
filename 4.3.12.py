# 4.3.12 Упаковка дубликатов 🌶️
#
# На вход программе подается строка текста, содержащая символы.
# Напишите программу, которая упаковывает последовательности
# одинаковых символов заданной строки в подсписки.
# Формат входных данных
# На вход программе подается строка текста, содержащая символы,
# отделенные символом пробела.
# Формат выходных данных
# Программа должна вывести указанный вложенный список.

# v1
lst_inp = [i for i in input().split()]
lst = []
tmp = [lst_inp[0]]

for i in range(1, len(lst_inp)):
    if lst_inp[i] == lst_inp[i - 1]:
        tmp += lst_inp[i]
    else:
        lst.append(tmp)
        tmp = [lst_inp[i]]
lst.append(tmp)
print(lst)

# v2
res = []
for el in input().split():
    if res and el in res[-1]:
        res[-1].append(el)
    else:
        res.append([el])
print(res)
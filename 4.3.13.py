# 4.3.13 Разбиение на чанки 🌶️
# На вход программе подаются две строки, на одной символы, на другой число n. Из первой строки формируется список.
# Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска),
# а возвращает список из чанков указанной длины.
# Формат входных данных
# На вход программе подается строка текста, содержащая символы, отделенные символом пробела и число n на отдельной строке.
# Формат выходных данных
# Программа должна вывести указанный вложенный список.
# Примечание. Не забудьте вызвать функцию chunked(), чтобы вывести результат 😀.

def chunked(str, n):
    lst = []
    for i in range(0, len(str), n):
        if len(str[i:]) <= n:
            lst.append(str[i:])
        else:
            lst.append(str[i:i + n])
    print(lst)


str = input().split()
n = int(input())
chunked(str, n)

# 8.4.10 Все 10 цифр
# На вход подаются две строки, состоящие из цифр.
# YES, если в записи этих двух строк используются все десять цифр, и NO в противном случае.
print(('NO', 'YES')[len(set(input() + input())) == 10])


# 8.4.16 подается строка, состоящая из трех слов.
# Если для слов был использован один и тот же набор букв == YES
a, b, c = map(set, input().split())
print('YES' if a == b == c else 'NO')


# 8.5.11 Уникальные символы 1
# Подается число n – общее количество слов. Далее идут n строк с словами.
print(*[len(set(input().lower())) for i in range(int(input()))], sep='\n')


# 8.5.12 Уникальные символы 2
# общее количество уникальных символов во всех словах без учета регистра.
# v1
set_ch = set()
for i in range(int(input())):
    set_ch.update(set(input().lower()))
print(len(set_ch))
# v2
print(len(set(''.join([input().lower() for _ in range(int(input()))]))))


# 8.5.13 Количество слов в тексте
# Напишите программу для определения общего количества различных слов в строке текста.
import re
print(len(set(re.sub(r'[.,;:-?!]', '', input().lower()).split())))


# 8.5.14 Встречалось ли число раньше?
# мое примечание: приводим к int, т.к. требуется отсечение нулей перед '002'
# v1 сравнение set до и после
inputs = input().split()
set_elem = set()
for i in inputs:
    tmp = set_elem.copy()
    set_elem.add(int(i))
    print('YES' if tmp == set_elem else 'NO')


# v2 проверка вхождения
set_elem = set()
for i in map(int, input().split()):
    # i in set_elem возвращает False\True -> False == 0 == NO
    print(['NO', 'YES'][i in set_elem])
    set_elem.add(i)

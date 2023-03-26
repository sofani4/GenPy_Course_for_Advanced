# 6.3.4 произведение элементов кортежа numbers.
# numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
# mult = 1
# print([mult := mult * i for i in numbers][-1])

# 6.3.9 Конкурсный отбор
# Напишите программу, которая выводит весь список, а потом список хорошистов и отличников в классе.
lst = [input().split() for i in range(int(input()))]

[print(*i) for i in lst]
print()
[print(*i) for i in lst if i[1] in ('45')]

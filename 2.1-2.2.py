# # 2.1.4 Стоимость строки
# # любой символ (в том числе пробел) стоит 6060 копеек
price = 60 * len(input())
print(f'{price // 100} р. {price % 100} коп.')

# # 2.1.6 Китайский гороскоп
animals = ["Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух",
           "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц"]

print(animals[int(input('Введите год: ')) % 12 - 8])

# 2.2.6 Произведение чисел
# В первой строке подаётся число n(0<n<1000) – количество чисел в наборе.
# В последующих nn строках вводятся целые числа,составляющие набор
# (могут повторяться). Затем следует целое число,которое является
# или не является произведением двух каких-то чисел из набора.
set_n = [int(input()) for n in range(int(input()))]
n = int(input())
flag = False

for i in range(len(set_n)):
    for j in range(i + 1, len(set_n)):
        if set_n[i] * set_n[j] == n:
            flag = True
            break

print('ДА' if flag else 'НЕТ')


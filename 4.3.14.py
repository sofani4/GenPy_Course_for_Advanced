# 4.3.14 Подсписки списка 🌶️🌶️
# Подсписок — часть другого списка. Подсписок может содержать один элемент, несколько, и даже ни одного.
# Например, [1], [2], [3] и [4] — подсписки списка [1, 2, 3, 4]. Список [2, 3] — подсписок списка [1, 2, 3, 4],
# но список [2, 4] не подсписок списка [1, 2, 3, 4], так как элементы 2 и 4 во втором списке не смежные.
# Пустой список — подсписок любого списка. Сам список — подсписок самого себя, то есть список [1, 2, 3, 4] подсписок списка [1, 2, 3, 4].
#
# На вход программе подается строка текста, содержащая символы. Из данной строки формируется список.
# Напишите программу, которая выводит список, содержащий все возможные подсписки списка, включая пустой список.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая символы, отделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести указанный список, содержащий все возможные подсписки,
# включая пустой список в соответствии с примерами.
#
# входные 1 2 3 4
# выходные [[], ['1'], ['2'], ['3'], ['4'], ['1', '2'], ['2', '3'], ['3', '4'], ['1', '2', '3'], ['2', '3', '4'], ['1', '2', '3', '4']]

# v1
def list_sublists(orig_lst):
    lst = [[]]
    amount = 0
    for i in range(1, len(orig_lst)):
        for j in range(len(orig_lst)):
            if len(orig_lst[j:j + i]) == i:
                lst.append(orig_lst[j:j + i])
            amount += 1
    lst.append(orig_lst)
    print(lst)


list_sublists(input().split())


# v2
def list_sublists2(orig_lst):
    new_lst = [[]]
    for i in range(1, len(orig_lst) + 1):
        # ограничение на j: не привышая необходимых границ
        for j in range(len(orig_lst) - i + 1):
            new_lst.append(orig_lst[j:j + i])
    print(new_lst)


list_sublists2(input().split())

# 2.2.11 Роскомнадзор запретил букву а 🌶️🌶️
# Необходимо написать программу, реализующую алгоритм написания этой песни.
# Алгоритм выводит в конце предложения следующую в алфавитном порядке букву,
# если она встречается в строке текста, а очередную строку отображает уже без этой буквы.
#
# Формат входных данных
# На вход программе подается одно слово, записанное строчными русскими буквами без буквы 'ё'.
#
# Формат выходных данных
# Программа должна вывести в соответствии с указанным алгоритмом строки,
# количество которых равно количеству разных букв в строке,
# которая получается путем конкатенации введенного слова и строки 'запретил букву'.

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
            'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
str = input() + ' запретил букву '

for i in range(len(alphabet)):
    if str == '':
        break
    elif str.count(alphabet[i]) > 0:
        print(str + alphabet[i])
        str = str.replace(alphabet[i], '').lstrip().replace('  ', ' ')

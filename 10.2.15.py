# 10.2.15 Набор сообщений
# программа, которая отображает нажатия клавиш, необходимые для
# введенного сообщения с кнопочного телефона

buttons = {
    '1': ['.', ',', '?', '!', ':'],
    '2': ['A', 'B', 'C'],
    '3': ['D', 'E', 'F'],
    '4': ['G', 'H', 'I'],
    '5': ['J', 'K', 'L'],
    '6': ['M', 'N', 'O'],
    '7': ['P', 'Q', 'R', 'S'],
    '8': ['T', 'U', 'V'],
    '9': ['W', 'X', 'Y', 'Z'],
    '0': [' ']
}

for i in input().upper():
    for key, value in buttons.items():
        if i in value:
            print(key*(value.index(i)+1), end='')
            break

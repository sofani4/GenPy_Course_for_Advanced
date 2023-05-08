# 8.6.13 Количество совпадающих
# вывести кол-во чисел, содержащихся одновременно как в первой строке, так и во второй строке
# v1
myset = set(input().split()).intersection(input().split())
print(len(myset))
# v2
print(len(set(input().split()) & set(input().split())))

# # 8.6.14 множество чисел, встречающихся в обеих строках.
# key=int - сортировка по числовым значениям элементов
print(*sorted(set(input().split()) & set(input().split()), key=int))

# # 8.6.16 Общие цифры
# # натуральное число n≥1, а затем n различных натуральных чисел, каждое на отдельной строке.
first_line = set()
for i in range(int(input())):
    if i == 0:
        first_line = set(input())
    else:
        first_line &= set(input())
print(*sorted(first_line))

# 8.7.7 Одинаковые цифры (есть ли в числах одинаковые цифры)
print('NO' if set(input()).isdisjoint(set(input())) else 'YES')

# 8.7.8 YES, если в запись первого числа входят все цифры,
# содержащиеся в записи второго числа и NO в противном случае.
# массив, и индекс как False == 0 \ True == 1
print(['NO', 'YES'][set(input()).issuperset(input())])

# 8.7.10 Программа, которая выводит множество оценок,
# которые есть и у первого и у второго учеников,
# но которых нет у третьего ученика
a, b, c = (set(input().split()) for _ in range(3))
print(*sorted((a & b) - c, reverse=True, key=int))

# 8.7.11 Вывести такие оценки, которые встречаются
# не более, чем у двух учеников.
a, b, c = (set(input().split()) for _ in range(3))
print(*sorted((a | b | c) - (a & b & c), key=int))

# 8.7.12 Программа, которая выводит множество оценок третьего ученика,
# которые не встречаются ни у первого, ни у второго ученика.
a, b, c = (set(input().split()) for _ in range(3))
print(*sorted(c - b - a, reverse=True, key=int))

# 8.7.13 Программа, которая выводит множество оценок,
# не встречающихся ни у одного из трех учеников.
a, b, c = (set(input().split()) for _ in range(3))
set_scores = set(str(i) for i in range(11))
print(*sorted(set_scores - (c | b | a), key=int))

# 8.8.6 получить множество, содержащее уникальные слова  строки sentence длиною меньше 44 символов.
sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
import re  # v1

stroka = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", '', sentence)
spisok = stroka.lower().split()
myset = {i for i in spisok if len(i) < 4}
print(*sorted(myset))

# v2 без регулярого выражения
sentence = sentence.split()
sentence = {w.strip('.,(:;)').lower() for w in sentence}
sentence = {w for w in sentence if len(w) < 4}
print(*sorted(sentence))

# 8.8.7 уникальные имена файлов c расширением .png, независимо от регистра имен и расширений
files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT',
         'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py',
         'stepik.org', 'kotlin.ko', 'github.git']
result = {c.lower() for c in files if c.lower().endswith('.png')}
print(*sorted(result))

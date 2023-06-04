# 10.3.11 Объединить содержимое двух словарей dict1 и dict2 по ключам, складывая значения
# по одному и тому же ключу, в случае, если ключ присутствует в обоих словарях.

dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
result = dict1.copy()
for key, value in dict2.items():
    result[key] = result.get(key, 0) + value
# get(), ищет значение по ключу, и если его нет, то возвращает значение переданное вторым аргументом.
# setdefault() также ищет значение по ключу, и если его нет, то сперва создает в словаре запись с таким ключом-значение, а потом уже возвращает значение.


# 10.3.12 Для каждого символа строки text подсчитать количество его вхождений и записать в словарь

text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
result = {}
for i in text:
    result[i] = result.setdefault(i, 0) + 1
print(result)


# 10.3.13 Вывести наиболее часто встречающееся слово строки s.
# Если таких слов несколько, вывести меньшее в лексикографическом порядке.

s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

result = {}
for i in s.split():
    result[i] = result.setdefault(i, 0) + 1
max_value = max(result.values())
print(min(key for key, values in result.items() if values == max_value))


# 10.3.14 В переменную result записать словарь, в котором для каждого владельца будут перечислены его собаки.
# Ключом словаря должен быть кортеж (имя, фамилия, возраст владельца),
# а значением – список кличек собак (сохранив исходный порядок следования).

pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}
for i in pets:
    #v1 result[i[1:]] = result.setdefault(i[1:], []) + [i[0]]
    result.setdefault(i[1:], []).append(i[0])
print(result)


# 10.3.15 Самое редкое слово 🌶️ (если несколько, то минимальное из них)

lst = [word.strip('.,!?:;-') for word in input().lower().split()]
result = {}
for i in lst:
    result[i] = result.setdefault(i, 0) + 1
max_value = min(result.values())
print(min(key for key, values in result.items() if values == max_value))


# 10.3.16 Исправление дубликатов 🌶️
# Добавлять к повтояющимся словам префикс кол-ва повторений

lst = [word for word in input().split()]
result = {}
for i in lst:
    result[i] = result.setdefault(i, -1) + 1
    print(i if result[i] == 0 else i + '_' + str(result[i]), end=' ')

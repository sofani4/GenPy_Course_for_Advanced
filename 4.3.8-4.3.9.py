# # 4.3.8 Список по образцу 1
# # На вход программе подается число n.
# # Напишите программу, которая создает и выводит построчно список,
# # состоящий из nn списков [[1, 2, ..., n], ..., [1, 2, ..., n]].
# # v1
# n = int(input())
# lst = [i for i in range(1, n + 1)]
# print(*(lst for _ in range(1, n + 1)), sep='\n')
#
# # v2
# n = int(input())
# for _ in range(n):
#     print([i for i in range(1, n + 1)])

# 4.3.9 Список по образцу 2
# На вход программе подается число nn. Напишите программу,
# которая создает и выводит построчно вложенный список,
# состоящий из nn списков [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]]

# v1
# tmp = 2
# n = int(input()) + 1
# while tmp <= n:
#     print([i for i in range(1, tmp)])
#     tmp += 1
#
# # v2
# n = int(input())
# result = []
# for i in range(1, n + 1):
#     result.append(list(range(1, i + 1)))
# print(*result, sep='\n')
#
# # v3
# for i in range(1, int(input()) + 1):
#     print([j for j in range(1, i + 1)])
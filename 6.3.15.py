# Последовательность Трибоначчи
# последовательность натуральных чисел, где каждое последующее число является суммой трех предыдущих:
# Sample Input 1: 10
# Sample Output 1: 1 1 1 3 5 9 17 31 57


# def tribonacci(n):
#     lst = [1, 1, 1]
#     if n > 3:
#         for i in range(3, n):
#             lst.append(lst[i - 1] + lst[i - 2] + lst[i - 3])
#     return tuple(lst[:n])
#
#
# print(*tribonacci(int(input())))

n = int(input())
t1 = t2 = t3 = 1
for _ in range(n):
    print(t1, end=' ')
    t1, t2, t3 = t2, t3, t1 + t2 + t3
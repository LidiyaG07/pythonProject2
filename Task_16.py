# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 3
# -> 1


import random

N = int(input("Введите количество элементов в массиве "))
list = [random.randint(1, 20) for i in range(N)]
print(list)
x = int(input("Введите искомое число "))
count = 0
for i in list:
    if i == x:
        count += 1
print(count)
# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
#     5
#     1 2 3 4 5
#     3
#     -> 1

import random

number = int(input('Ведите число элементов: '))

myList = []
for i in range(number):
    myList.append(random.randrange(0, 10))

print(myList)

findNumber = int(input('Ведите некоторое число Х: '))

sumX = 0
for i in myList:
    if i == findNumber:
        sumX += 1

print(f'Число "{findNumber}" встречается {sumX} раз(а).')

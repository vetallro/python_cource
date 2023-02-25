# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
#     5
#     1 2 3 4 5
#     6
#     -> 5

import random
number = int(input('Ведите число элементов: '))

myList = []
for i in range(number):
    myList.append(random.randrange(0, 1000))
print(myList)

findNumber = int(input('Ведите некоторое число Х: '))

closeNumberIndex = myList[1]
minDelta = 10000
for i in range(len(myList)):
    if abs(myList[i] - findNumber) < minDelta:
        minDelta = abs(myList[i] - findNumber)
        closeNumberIndex = i

print(f'Число {myList[closeNumberIndex]} ближе всего к {findNumber}.')

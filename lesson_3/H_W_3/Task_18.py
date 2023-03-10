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


# myList = [2, 7, 6, 8, 3, 4, 8, 8, 1, 0]

def inputnumber(message):
    number = int(input(message))
    return number


numberInList = inputnumber('Ведите число элементов: ')
myList = []
for i in range(numberInList):
    myList.append(random.randrange(0, 10))
print(myList)

numberToFind = inputnumber('Ведите некоторое число Х: ')

closeNumberIndex = 0
minDelta = 10000

for i in range(len(myList)):
    if abs(myList[i] - numberToFind) < minDelta:
        minDelta = abs(myList[i] - numberToFind)
        closeNumberIndex = i

print(f'Число {myList[closeNumberIndex]} ближе всего к {numberToFind}.')

# Ведите число элементов: 10
# [2, 7, 6, 8, 3, 4, 8, 8, 1, 0]
# Ведите некоторое число Х: 5
# Число 8 ближе всего к 5.

# from random import randint
#
# n = int(input())
# list_nums = [randint(1, 50) for _ in range(n)]
#
# print(list_nums)
#
# b = int(input())
# m = min(list_nums, key=lambda x: abs(x - b))
#
# print(m)

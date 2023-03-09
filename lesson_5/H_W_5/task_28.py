# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух
# целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
#
#       *Пример:*
#
#       2 2
#       4

def sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return sum(a + 1, b - 1)


a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

print(f'Сумма чисел А и В: {sum(a, b)}')
# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list_one = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = int(input("Введите минимум: "))
max_number = int(input("Введите максимум: "))
output_1 = []
for i in range(len(list_one)):
    if min_number <= list_one[i] <= max_number:
        output_1.append(i)
print(output_1)
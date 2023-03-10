# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

print('Элементы первого множества')
set1 = set(int(input()) for i in range(n))
print(set1)
print('Элементы второго множества')
set2 = set(int(input()) for i in range(m))
print(set2)
result_set = set1.intersection(set2)
result_list = sorted(list(result_set))

print("Результат: ")
for item in result_list:
    print(item)

# Пользователь вводит текст(строка).
# Словом считается последовательность непробельных
# символов идущих подряд, слова разделены одним
# или большим числом пробелов.
# Определите, сколько различных слов содержится в этом тексте.

# Input: She sells sea shells on the sea shore
# The shells that she sells are sea shells
# I'm sure.So if she sells sea shells on
# the sea shore I'm sure that the
# shells are sea shore shells

# A = set(input('Введите строку: ').lower().split())
# print(len(A))

# ---------------------------------------------------

# text = input().split()
# print(text)
# my_dict = {}
#
# for i in text:
#     if i in my_dict:
#         print(f'{i}_{my_dict[i]}', end=' ')
#     else:
#         print(i, end=' ')
#     my_dict[i] = my_dict.get(i, 0) + 1

# ---------------------------------------------------

# Ваня и Петя поспорили, кто быстрее решит следующую задачу:
# “Задана последовательность неотрицательных целых чисел.
# Требуется определить значение наибольшего элемента последовательности,
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”.
# Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать
# это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор.
# За помощью товарищи обратились к Вам, студентам.

# ---------------------------------------------------

# неверное решение
# Ваня

# n = int(input())
# max_number = 1000
# while n != 0:
#     n = int(input())
#     if max_number > n:
#     max_number = n
# print(max_number)

# Petya
# ---------------------------------------------------
# неверное решение

# n = int(input())
# max_number = -1
# while n < 0:
#     n = int(input())
#     if max_number < n:
#     n = max_number
# print(n)

# ---------------------------------------------------
# верное решение
# Ваня

# flag = True
# max_number = 0
# while flag:
#     n = int(input())
#     if max_number < n:
#         max_number = n
#     if n == 0:
#         flag = False
# print(max_number)

# ---------------------------------------------------


# 8cKr&HgTC9bVbs8
# P9dc6Z5CTx4.C3Q
#  API chatGPT       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
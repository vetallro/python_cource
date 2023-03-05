# # проверить сколько уникальных значений в списке.
#
# listNums = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]
# print(len(set(listNums)))
#

# k = int(input('Введите сдвиг: '))
#
# listNums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# print(listNums)
#
# for i in range(k):
#     listNums.insert(0, listNums.pop(   -1))
#
# print(listNums)

# list_dict = [{"V": "S001"}, {"V": "S002"},
#              {"VI": "S001"}, {"VI": "S005"},
#              {"VII": " S005 "}, {"V": " S009 "},
#              {"VIII": " S007 "}]
#
# for i in list_dict:
#     print(list(i.values())[0].strip())


# n = [int(i) for i in input().split()]
n = list(map(int, input().split()))
print(n)

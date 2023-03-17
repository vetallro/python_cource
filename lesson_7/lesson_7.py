# values = [1, 23, 42, 'asdfg']
#
# transformation = lambda x: x
# transformed_values = list(map(transformation, values))
#
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')
#
# def find_farthest_orbit(orbits):
#     max = i
#     for i in orbits:
#         if i[1] != i[2]:
#             s = i[1] * i[2]
#
#
# def make_dict(li):
#     dict_1 = {i[0] * i[1]: i for i in li if i[0] != i[1]}
#     return dict_1
#
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(make_dict(orbits))
# print(*max(make_dict(orbits).items())[1])


# print(*find_farthest_orbit(orbits))

# def func(li):
# dict = {i[0] * i[1]: i for i in li if i[0] != i[1]}
#
# return max(dict.items())[1]
#
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (11, 11)]
#
# print(*func(orbits))

# print(sum([i[1] for i in scrabble.items() for j in word if j.upper() in i[0]]))


# def same_by(condition, nums):

def same_by(characteristic, objects):
    return len(set(map(characteristic, objects))) == 1


# values = [2, 3, 6, 4]
values = [2, 2, 2, 2]

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')



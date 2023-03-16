def calc1(a, b):
    return a + b


def calc2(a, b):
    return a * b


def math(op, x, y):
    return (op(x, y))


# print(math(calc1, 5, 4))

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
#
# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))
#
# print(res)

def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x ** 2), res))
print(res)

list_1 = [x for x in range(1, 20)]
print(list_1)
list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)
list_1 = filter(lambda x: x % 2 == 0, list_1)
print(list_1)
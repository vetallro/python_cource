#
#
#
#
#
import random

myList = []
oneList = list()
twoList = [1, 3, 4, 5, 3, 2, 4]
print(twoList)
print(*twoList)

for i in range(20):
    myList.append(random.randrange(100))

print(myList)
print(*myList)
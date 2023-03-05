number = int(input("Введите число: "))
result = 0
b = 0
for i in range(number):
    temp = int(input("Введите температуру"))
    if temp >= 0:
        result += 1
    else:
        if result > b:
            b = result
        result = 0
print(b)

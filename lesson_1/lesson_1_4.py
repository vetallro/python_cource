
year = int(input('Введите год для проверки: '))

while year / 1000 < 1:
    print('введите в формате YYYY.')
    print()
    year = int(input('Введите год для проверки: '))
    print()

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('Yes')
else:
    print('No')


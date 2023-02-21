ticketNumber = int(input('Введите вагон по билету: '))
factNumber = int(input('Введите вагон по счету: '))

if ticketNumber == factNumber:
    print('Недостаточно данных для расчета.')
else:
    print('Количество вагонов поезда:', ticketNumber + factNumber - 1)
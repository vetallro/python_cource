# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое
# содержит либо только английские, либо только русские буквы.
#
#      *Пример:*
#       ноутбук
#       12

score1 = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т', 'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']  # 1 очко;
score2 = ['Д', 'К', 'Л', 'М', 'П', 'У', 'D', 'G']  # 2 очка;
score3 = ['Б', 'Г', 'Ё', 'Ь', 'Я', 'B', 'C', 'M', 'P']  # 3 очка;
score4 = ['Й', 'Ы', 'F', 'H', 'V', 'W', 'Y']  # 4 очка;
score5 = ['Ж', 'З', 'Х', 'Ц', 'Ч', 'K']  # 5 очков;
score8 = ['Ш', 'Э', 'Ю', 'J', 'X']  # 8 очков;
score10 = ['Ф', 'Щ', 'Ъ', 'Q', 'Z']  # 10 очков.

word = input('Введите слово: ').upper()

total = 0
for i in word:
    if i in score1:
        total += 1
    elif i in score2:
        total += 2
    elif i in score3:
        total += 3
    elif i in score4:
        total += 4
    elif i in score5:
        total += 5
    elif i in score8:
        total += 8
    elif i in score10:
        total += 10

print(f'Вес слова: {total}')

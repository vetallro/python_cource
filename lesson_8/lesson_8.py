# эталонное решение ДЗ - разбор на следующем семинаре

alp = 'аяуюоеёэиы'
word_sug = input().split()
# vowel_letters = [word.count(char) for word in word_sug for char in word if char.lower() in alp]

vowel_letters = []

for word in word_sug:
    for char in word.lower():
        if char in alp:
            vowel_letters.append(char.count(char))

print(set(vowel_letters))
print(len(set(vowel_letters)))
if len(set(vowel_letters)) == 1:
    print('Парам-пам-пам')
else:
    print('Пам парам')




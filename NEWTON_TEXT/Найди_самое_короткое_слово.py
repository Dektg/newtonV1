print('Привет, я Ньютон. В этой программе я могу посчитать\n\
количество символов самого маленького слова в тексте.')
string = input('Введите текст: ')

words = string.split()

shortest = words[0]

for i in words[1:]:
    if len(i) < len(shortest):
        shortest = i

print(shortest, ':', len(shortest), end='')
x = len(shortest) + 1
if 11 <= x <= 19:
    print(" символов")
else:
    if x % 10 == 1:
        print(" символ")
    else:
        if 2 <= x % 10 <= 4:
            print(" символа")
        else:
            print(" символов")

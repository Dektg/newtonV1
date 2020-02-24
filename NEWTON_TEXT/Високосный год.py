print('Привет, я Ньютон. В этой программе я могу\n\
сказать, является ли ваш год високосным.')
text = input('Введите ваш год: ')
text = int(text)

if text % 400 == 0:
    print(text, " Да")
else:
    if text % 4 == 0 and text % 100 != 0:
        print(text, " Да")
    else:
        print(text, " Нет")
print('Привет, я Ньютон. В этой программе я могу\n\
сказать вам, подходит ли файл для указанного расширения.')
extensions = ['png', 'jpg', 'jpeg', 'gif', 'svg']

file = input('Введите имя файла с расширением: ').split('.')
if len(file) >= 2:
    fileExtension = file[-1].lower()
    if fileExtension in extensions:
        print("Да")
    else:
        print("Нет")
else:
    print("Расширение файла не соответствует норме")

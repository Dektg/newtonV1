while True:
    srte = input('Введите текст: ')

    f = open('some.txt', 'a')
    f.write(srte)
    f.close()

    fr = open('some.txt', 'r')
    text = fr.read()
    fr.close()

    print(text)

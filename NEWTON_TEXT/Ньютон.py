import math, os


def talk(words):
    os.system("say " + words)  # Проговариваем слова


while True:
    operation = input('Что мне сделать: ').lower()
    operation_w = operation.split(' ')

    for list_of_numbers in operation_w:
        if 'процент' == list_of_numbers or 'процентов' == list_of_numbers or 'проценты' == list_of_numbers:
            def PERCENT():
                num = int(input('Введи число: '))
                percent = float(input('Введите процент от числа: '))
                print(percent, ' % от ', num, ' = ', (num * percent) / 100, sep='')
                talk(str((num * percent) / 100))


            PERCENT()

        if 'горизонт' == list_of_numbers or 'горизонд' == list_of_numbers or 'горизонта' == list_of_numbers or 'горизонда' == list_of_numbers:
            def horizon():
                print('                       l = √2Rh')
                R = 6371
                talk('Сэр скажите высоту')
                h = input('Введите высоту над уровнем моря: ')
                sign = h[-2:]
                sign2 = h[-1]
                if sign == 'км' or sign == 'km':
                    h = int(h[:-2])
                elif sign2 == 'м' or sign2 == 'm':
                    h = int(h[:-1]) / 1000

                l = math.sqrt(2 * R * h)
                print('l =', round(l), 'км =', round(l * 1000), 'м')
                talk(str(round(l)) + 'км')


            horizon()

        if 'большую' == list_of_numbers or 'максимальную' == list_of_numbers:
            def min_number_in_number():
                num = float(input('Введите ваше число: '))
                strNum = str(num)

                maxDigit = -1

                for i in range(len(strNum)):
                    if strNum[i] == '.':
                        continue
                    elif maxDigit < int(strNum[i]):
                        maxDigit = int(strNum[i])
                print('Цыфра:', maxDigit)
                talk('Цыфра ' + str(maxDigit))


            min_number_in_number()

        if 'квадратного' == list_of_numbers or 'квадратное' == list_of_numbers or 'квадратный' == list_of_numbers:
            import math, os


            def talk(words):
                os.system("say " + words)  # Проговариваем слова


            def quadratic_equation():
                print('a * x² + b * x + c = 0')
                a = int(input('a: '))
                b = int(input('b: '))
                c = int(input('c: '))
                if a != 0 and b != 0 and c != 0:
                    if a == 0:
                        print('Это не квадратное уравнение')
                        talk('Это не квадратное уравнение')
                    if b < 0:
                        bs = '(' + str(b) + ')'
                    else:
                        bs = ''
                    D = b * b - 4 * a * c
                    print('D = b² - 4 * a * c = ⋅⋅⋅ \n\
            ⋅⋅⋅ = ', bs, '² - 4 * ', a, ' * ', c, ' = ', D, sep='')
                    if D < 0:
                        print('У уравнения нет корней')
                        talk('У. Уравнения нет корней')
                    if D > 0:
                        x1 = (-b - math.sqrt(D)) / (2 * a)
                        if (len(str(x1).split('.')[1])) > 3:
                            about_x1 = ' ≈ ' + str(round(x1, 3))
                            about_x1_talk = str(about_x1[3:])

                            if type(round(x1, 3)) == float:
                                massiv = about_x1_talk.split('.')
                                massiv.insert(1, ' точка ')
                                if len(massiv[2]) == 1:
                                    massiv.insert(3, ' десятых')
                                if len(massiv[2]) == 2:
                                    massiv.insert(3, ' сотых')
                                if len(massiv[2]) == 3:
                                    massiv.insert(3, ' тысячных')
                                about_x1_talk = ''.join(massiv)

                            if about_x1_talk[0] == '-':
                                about_x1_talk = 'минус ' + about_x1_talk[1:]
                        else:
                            about_x1 = ''
                            about_x1_talk = str(x1)
                            massiv = about_x1_talk.split('.')
                            if massiv[1] == '0':
                                about_x1_talk = about_x1_talk[:-2]
                            else:
                                if type(x1) == float:
                                    massiv.insert(1, ' точка ')
                                    if len(massiv[2]) == 1:
                                        massiv.insert(3, ' десятых')
                                    if len(massiv[2]) == 2:
                                        massiv.insert(3, ' сотых')
                                    if len(massiv[2]) == 3:
                                        massiv.insert(3, ' тысячных')
                                    about_x1_talk = ''.join(massiv)
                            if about_x1_talk[0] == '-':
                                about_x1_talk = 'минус ' + about_x1_talk[1:]

                        x2 = (-b + math.sqrt(D)) / (2 * a)
                        if (len(str(x2).split('.')[1])) > 3:
                            about_x2 = ' ≈ ' + str(round(x2, 3))
                            about_x2_talk = str(about_x2[3:])
                            if type(round(x2, 3)) == float:
                                massiv = about_x2_talk.split('.')
                                massiv.insert(1, ' точка ')
                                if len(massiv[2]) == 1:
                                    massiv.insert(3, ' десятых')
                                if len(massiv[2]) == 2:
                                    massiv.insert(3, ' сотых')
                                if len(massiv[2]) == 3:
                                    massiv.insert(3, ' тысячных')
                                about_x2_talk = ''.join(massiv)
                            if about_x2_talk[0] == '-':
                                about_x2_talk = 'минус ' + about_x2_talk[1:]
                        else:
                            about_x2 = ''
                            about_x2_talk = str(x2)
                            massiv = about_x2_talk.split('.')
                            if massiv[1] == '0':
                                about_x2_talk = about_x2_talk[:-2]
                            else:
                                if type(x2) == float:
                                    massiv.insert(1, ' точка ')
                                    if len(massiv[2]) == 1:
                                        massiv.insert(3, ' десятых')
                                    if len(massiv[2]) == 2:
                                        massiv.insert(3, ' сотых')
                                    if len(massiv[2]) == 3:
                                        massiv.insert(3, ' тысячных')
                                    about_x2_talk = ''.join(massiv)
                            if about_x2_talk[0] == '-':
                                about_x2_talk = 'минус ' + about_x2_talk[1:]
                        print('\n      -b + √D      ', -b, ' + √', D, '\nx₁ = --------- = ----------- = ', x1, about_x1,
                              '\n        2 * a       2 * ', a, '\n', sep='')
                        print('\n      -b - √D      ', -b, ' - √', D, '\nx₂ = --------- = ----------- = ', x2, about_x2,
                              '\n        2 * a       2 * ', a, '\n', sep='')
                        talk('x первый равен ' + str(about_x1_talk))
                        talk('x второй равен ' + str(about_x2_talk))
                    if D == 0:
                        x = -b / (2 * a)
                        print('x = -b / (2 * a) =', x)
                        about_x_talk = str(x)
                        massiv = about_x_talk.split('.')
                        if massiv[1] == '0':
                            about_x_talk = about_x_talk[:-2]
                        else:
                            if type(x) == float:
                                massiv.insert(1, ' точка ')
                                if len(massiv[2]) == 1:
                                    massiv.insert(3, ' десятых')
                                if len(massiv[2]) == 2:
                                    massiv.insert(3, ' сотых')
                                if len(massiv[2]) == 3:
                                    massiv.insert(3, ' тысячных')
                                about_x_talk = ''.join(massiv)
                        if about_x_talk[0] == '-':
                            about_x_talk = 'минус ' + about_x_talk[1:]
                        talk('x равен ' + about_x_talk)
                elif b == 0 and c == 0:
                    print(a, ' * x² = 0\n\
            x = 0', sep='')
                    talk('x, равен нулю')

                elif c == 0:
                    x2 = -b / a
                    print(a, ' * x² + ', b, ' * x = 0\n\
            x₁ = 0      ', a, ' * x₂ + ', b, ' = 0\n\
            ', a, ' * x₂ = ', -b, '\n\
            x₂ = ', -b, ' / ', a, ' = ', x2, sep='')
                    talk('x первый равен нулю')
                    talk('x второй равен' + str(x2))
                elif b == 0:

                    ca = round(c / a)
                    if ca < 0:
                        print('Это не квадратное уравнение')
                        talk('Это не квадратное уравнение')
                        exit(0)
                    x1 = math.sqrt(ca)
                    if (len(str(x1).split('.')[1])) > 3:
                        about_x1 = ' ≈ ' + str(round(x1, 3))
                        about_x1_talk = str(about_x1[3:])
                        if type(round(x1, 3)) == float:
                            massiv = about_x1_talk.split('.')
                            massiv.insert(1, ' точка ')
                            if len(massiv[2]) == 1:
                                massiv.insert(3, ' десятых')
                            if len(massiv[2]) == 2:
                                massiv.insert(3, ' сотых')
                            if len(massiv[2]) == 3:
                                massiv.insert(3, ' тысячных')
                            about_x1_talk = ''.join(massiv)
                        if about_x1_talk[0] == '-':
                            about_x1_talk = 'минус ' + about_x1_talk[1:]
                    else:
                        about_x1 = ''
                        about_x1_talk = str(x1)
                        massiv = about_x1_talk.split('.')
                        if massiv[1] == '0':
                            about_x1_talk = about_x1_talk[:-2]
                        else:
                            if type(x1) == float:
                                massiv.insert(1, ' точка ')
                                if len(massiv[2]) == 1:
                                    massiv.insert(3, ' десятых')
                                if len(massiv[2]) == 2:
                                    massiv.insert(3, ' сотых')
                                if len(massiv[2]) == 3:
                                    massiv.insert(3, ' тысячных')
                                about_x1_talk = ''.join(massiv)
                        if about_x1_talk[0] == '-':
                            about_x1_talk = 'минус ' + about_x1_talk[1:]

                    x2 = -math.sqrt(ca)
                    if (len(str(x2).split('.')[1])) > 3:
                        about_x2 = ' ≈ ' + str(round(x2, 3))
                        about_x2_talk = str(about_x2[3:])
                        if type(round(x2, 3)) == float:
                            massiv = about_x2_talk.split('.')
                            massiv.insert(1, ' точка ')
                            if len(massiv[2]) == 1:
                                massiv.insert(3, ' десятых')
                            if len(massiv[2]) == 2:
                                massiv.insert(3, ' сотых')
                            if len(massiv[2]) == 3:
                                massiv.insert(3, ' тысячных')
                            about_x2_talk = ''.join(massiv)
                        if about_x2_talk[0] == '-':
                            about_x2_talk = 'минус ' + about_x2_talk[1:]
                    else:
                        about_x2 = ''
                        about_x2_talk = str(x2)
                        massiv = about_x1_talk.split('.')
                        if massiv[1] == '0':
                            about_x2_talk = about_x2_talk[:-2]
                        else:
                            if type(x2) == float:
                                massiv.insert(1, ' точка ')
                                if len(massiv[2]) == 1:
                                    massiv.insert(3, ' десятых')
                                if len(massiv[2]) == 2:
                                    massiv.insert(3, ' сотых')
                                if len(massiv[2]) == 3:
                                    massiv.insert(3, ' тысячных')
                                about_x2_talk = ''.join(massiv)
                        if about_x2_talk[0] == '-':
                            about_x2_talk = 'минус ' + about_x2_talk[1:]
                    print(a, ' * x² + ', c, ' = 0\n', a, ' * x² = ', -c, '\n\
            x² = ', -c, '/', a, '\n\
            x₁ = √', -c, '/', a, ' = ', x1, about_x1, '\n\
            x₂ = -√', -c, '/', a, ' = ', x2, about_x2, sep='')
                    talk('x первый равен' + about_x1_talk)
                    talk('x второй равен' + about_x2_talk)


            quadratic_equation()
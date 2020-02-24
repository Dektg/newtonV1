# -*- coding: utf-8 -*-
import math, os


from TALK import talk


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
        print('D = b² - 4 * a * c = ⋅⋅⋅ \n              ⋅⋅⋅ = ', bs, '² - 4 * ', a, ' * ', c, ' = ', D, sep='')
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
            print('\n      -b + √D     ', -b, ' + √', D, '\nx₁ = --------- = ','-' * (len(str(-b)) + len(str(D)) + 6), ' = ', x1, about_x1,
                  '\n        2 * a  ',' ' * int(((len(str(-b)) + len(str(D)) + 3)/2)), '2 * ', a, '\n', sep='')
            print('\n      -b - √D     ', -b, ' - √', D, '\nx₂ = --------- = ','-' * (len(str(-b)) + len(str(D)) + 6), ' = ', x2, about_x2,
                  '\n        2 * a  ',' ' * int(((len(str(-b)) + len(str(D)) + 3)/2)), '2 * ', a, '\n', sep='')
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
            talk('x равен '+ about_x_talk)
    elif b == 0 and c == 0:
        print(a,' * x² = 0\n\
x = 0', sep='')
        talk('x, равен нулю')

    elif c == 0:
        x2 = -b / a
        print(a, ' * x² + ', b, ' * x = 0\nx₁ = 0      ', a, ' * x₂ + ', b, ' = 0\n', a, ' * x₂ = ', -b, '\nx₂ = ', -b, ' / ', a, ' = ', x2, sep='')
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
        print(a, ' * x² + ', c, ' = 0\n', a, ' * x² = ', -c, '\nx² = ', -c, '/', a, '\nx₁ = √', -c, '/', a, ' = ', x1, about_x1, '\nx₂ = -√', -c, '/', a, ' = ', x2, about_x2, sep='')
        talk('x первый равен' + about_x1_talk)
        talk('x второй равен' + about_x2_talk)


quadratic_equation()
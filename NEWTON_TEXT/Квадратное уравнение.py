import math

print('Привет, я Ньютон. В этой программе я могу\n\
решить любое квадратное уравнение.\n\
Если уравнение не является полным, то там, где нет переменных, напиши ноль.')
print('a * x² + b * x + c = 0')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if a != 0 and b != 0 and c != 0:
    if a == 0:
        print('Это не квадратное уравнение')
        exit(0)
    if b < 0:
        bs = '(' + str(b) + ')'
    D = b * b - 4 * a * c
    print('D = b² - 4 * a * c = ⋅⋅⋅ \n\
                    ⋅⋅⋅ = ', bs, '² - 4 * ', a, ' * ', c, ' = ', D, sep='')
    if D < 0:
        print('У уравнения нет корней')
    if D > 0:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        if (len(str(x1).split('.')[1])) > 3:
            about_x1 = ' ≈ ' + str(round(x1, 3))
        else:
            about_x1 = ''
        x2 = (-b + math.sqrt(D)) / (2 * a)
        if (len(str(x2).split('.')[1])) > 3:
            about_x2 = ' ≈ ' + str(round(x2, 3))
        else:
            about_x2 = ''
        print('\n      -b + √D      ', -b, ' + √', D, '\n\
x₁ = --------- = ----------- = ', x1, about_x1, '\n\
        2 * a       2 * ', a, '\n', sep='')
        print('\n      -b - √D      ', -b, ' - √', D, '\n\
x₂ = --------- = ----------- = ', x2, about_x2, '\n\
        2 * a       2 * ', a, '\n', sep='')
    if D == 0:
        x = -b / (2 * a)
        print('x = -b / (2 * a) =', x)
elif b == 0 and c == 0:
    print('a * x² = 0\n\
x = 0', sep='')

elif c == 0:
    x2 = -b / a
    print(a, ' * x² + ', b, ' * x = 0\n\
x₁ = 0      ', a, ' * x₂ + ', b, ' = 0\n\
            ', a, ' * x₂ = ', -b, '\n\
            x₂ = ', -b, ' / ', a, ' = ', x2, sep='')
elif b == 0:

    ca = round(c / a)
    if ca < 0:
        print('Это не квадратное уравнение')
        exit(0)
    x1 = math.sqrt(ca)
    if (len(str(x1).split('.')[1])) > 3:
        about_x1 = ' ≈ ' + str(round(x1, 3))
    else:
        about_x1 = ''
    x2 = -math.sqrt(ca)
    if (len(str(x2).split('.')[1])) > 3:
        about_x2 = ' ≈ ' + str(round(x2, 3))
    else:
        about_x2 = ''
    print(a, ' * x² + ', c, ' = 0\n', a, ' * x² = ', -c, '\n\
x² = ', -c, '/', a, '\n\
x₁ = √', -c, '/', a, ' = ', x1, about_x1, '\n\
x₂ = -√', -c, '/', a, ' = ', x2, about_x2, sep='')

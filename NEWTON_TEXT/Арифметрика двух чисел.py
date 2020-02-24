print('Привет, я Ньютон. В этой программе я могу\n\
умножать, складывать, вычитать, делить два числа.')
a = input('Введите первое число: ')
a = int(a)
function_ab = input('Введите операцию: ')
b = input('Введите второе число: ')
b = int(b)


def arithmetic():
    if function_ab == '+':
        print(a + b)
    if function_ab == '-':
        print(a - b)
    if function_ab == '*':
        print(a * b)
    if function_ab == '/':
        print(a / b)
    if function_ab != '+' and function_ab != '-' and function_ab != '*' and function_ab != '/':
        print("Неизвестная операция")


arithmetic()

from math import sqrt
print('Привет, я Ньютон. В этой программе я могу\n\
найти периметр, площадь или диагональ квадрата по его стороне')
side = input('Введите сторону квадрата: ')
side = int(side)


def square_Print():
    print("Периметр = 4 * a =", side * 4)
    print("Площадь = a * a =", side ** 2)
    print("Диагональ = a * sqrt(2) =", sqrt(2) * side)


def square():
    answer = []
    answer.insert(0, side * 4)
    answer.insert(1, side ** 2)
    answer.insert(2, sqrt(2) * side)
    print(tuple(answer))


square_Print()
square()

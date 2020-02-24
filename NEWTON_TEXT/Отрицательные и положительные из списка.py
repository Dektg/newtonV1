import random
print('Привет, я Ньютон. В этой программе я могу найти\n\
отрицательные и положительные числа в списке.')

count = int(input('Сколько чисел будет в списке: '))
negative = []
positive = []

a = []
for i in range(count):
    a.append(int(random.random() * 20) - 10)
    if a[i] < 0:
        negative.append(a[i])
    if a[i] > 0:
        positive.append(a[i])
print('Исходный список: ', a, '\nОтрицательные: ', negative, '\nПоложительные: ', positive)

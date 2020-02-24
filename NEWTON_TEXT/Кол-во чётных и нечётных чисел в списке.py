from random import random

print('Привет, я Ньютон. В этой программе я могу\n\
разделять четные и нечетные числа из списка в разные списки.')

count = int(input('Введите кол-во чисел в списке: '))
roster = []
even = 0
odd = 0
for i in range(count):
    roster.append(int(random()*1000))
    if roster[i] % 2 == 0:
        even += 1
    else:
        odd += 1
print('Чётных: ', even, '\nНечётных: ', odd)

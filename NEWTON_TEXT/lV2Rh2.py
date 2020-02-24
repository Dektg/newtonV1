# -*- coding: utf-8 -*-
from math import sqrt

R = 6371
h = input('Введите высоту над уровнем моря: ')
sign = h[-2:]
sign2 = h[-1]
if sign == 'км' or sign == 'km':
    h = int(h[:-2])
elif sign2 == 'м' or sign2 == 'm':
    h = int(h[:-1]) / 1000

l = sqrt(2 * R * h)
print('l =',round(l), 'км =', round(l * 1000), 'м')

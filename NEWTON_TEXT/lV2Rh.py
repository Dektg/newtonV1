# -*- coding: utf-8 -*-
from math import sqrt

print('l = √2Rh')
Planet = input('\nНа какой вы планете: ').lower()
if Planet.find('земле') != -1 or Planet.find('земля') != -1 or Planet.find('земли') != -1:
    R = 6371
elif Planet.find('марсе') != -1 or Planet.find('марс') != -1 or Planet.find('марса') != -1:
    R = 3389.5
elif Planet.find('солнце') != -1 or Planet.find('солнца') != -1:
    R = 695510
elif Planet.find('юпитере') != -1 or Planet.find('юпитер') != -1 or Planet.find('юпитера') != -1:
    R = 69911
elif Planet.find('луне') != -1 or Planet.find('луна') != -1 or Planet.find('луны') != -1:
    R = 1737.1
elif Planet.find('сатурне') != -1 or Planet.find('сатурн') != -1 or Planet.find('сатурна') != -1:
    R = 58232
elif Planet.find('уране') != -1 or Planet.find('уран') != -1 or Planet.find('урана') != -1:
    R = 25362
elif Planet.find('венере') != -1 or Planet.find('венера') != -1 or Planet.find('венеры') != -1:
    R = 6051.8
elif Planet.find('меркурие') != -1 or Planet.find('меркурий') != -1 or Planet.find('меркурия') != -1:
    R = 2439.7
elif Planet.find('непруне') != -1 or Planet.find('нептун') != -1 or Planet.find('нептуна') != -1:
    R = 24622
elif Planet.find('плутоне') != -1 or Planet.find('плутон') != -1 or Planet.find('плутона') != -1:
    R = 1188.3
else:
    R = float(input('Введите радиус объекта на котором вы стоите: '))
print('R =', R, 'км')
h = input('Введите высоту над уровнем моря: ')
sign = h[-2:]
sign2 = h[-1]
if sign == 'км' or sign == 'km':
    h = int(h[:-2])
elif sign2 == 'м' or sign2 == 'm':
    h = int(h[:-1]) / 1000

l = sqrt(2 * R * h)
print('l =',round(l), 'км =', round(l * 1000), 'м')

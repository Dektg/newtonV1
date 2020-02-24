# -*- coding: utf-8 -*-
import random
from termcolor import cprint

a = random.randint(100, 1000)
b = random.randint(100, 1000)
c = a * b
ab = str(a) + ' * ' + str(b) + ' = '
user_response = input(ab)
if int(user_response) == c:
    cprint(' '* int(len(str(ab) + str(c))), 'green', 'on_green')
    print('\tВерно')
else:
    cprint(' '* int(len(str(ab) + str(c))), 'red', 'on_red')
    print('\tНе верно')
    print(ab , c, sep='')
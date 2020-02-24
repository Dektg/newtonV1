# -*- coding: utf-8 -*-
from A_command import mess
import os

from TALK import talk

mess_operation = mess.split(' ')
if any(map(str.isdigit, mess_operation[0])) == True and any(map(str.isdigit, mess_operation[-1])) == True:
    result_multiplication = (float(mess_operation[0])) * (float(mess_operation[-1]))
    print('{0:,}'.format(result_multiplication).replace(',', ' '))
    if type(result_multiplication) == float:
        result_multiplication = round(result_multiplication, 3)
        multiplication_talk = str(result_multiplication)
        massiv = multiplication_talk.split('.')
        if massiv[1] == '0':
            multiplication_talk = multiplication_talk[:-2]
        else:
            massiv.insert(1, ' точка ')
            if len(massiv[2]) == 1:
                massiv.insert(3, ' десятых')
            if len(massiv[2]) == 2:
                massiv.insert(3, ' сотых')
            if len(massiv[2]) == 3:
                massiv.insert(3, ' тысячных')
            multiplication_talk = ''.join(massiv)
        if multiplication_talk[0] == '-':
            multiplication_talk = 'минус ' + multiplication_talk[1:]
    talk(multiplication_talk)
if any(map(str.isdigit, mess_operation[1])) == True and any(map(str.isdigit, mess_operation[-1])) == True:
    result_multiplication = (float(mess_operation[1])) * (float(mess_operation[-1]))
    print('{0:,}'.format(result_multiplication).replace(',', ' '))
    if type(result_multiplication) == float:
        result_multiplication = round(result_multiplication, 3)
        multiplication_talk = str(result_multiplication)
        massiv = multiplication_talk.split('.')
        if massiv[1] == '0':
            multiplication_talk = multiplication_talk[:-2]
        else:
            massiv.insert(1, ' точка ')
            if len(massiv[2]) == 1:
                massiv.insert(3, ' десятых')
            if len(massiv[2]) == 2:
                massiv.insert(3, ' сотых')
            if len(massiv[2]) == 3:
                massiv.insert(3, ' тысячных')
            multiplication_talk = ''.join(massiv)
        if multiplication_talk[0] == '-':
            multiplication_talk = 'минус ' + multiplication_talk[1:]
    talk(multiplication_talk)


# -*- coding: utf-8 -*-
from A_command import mess
from TALK import talk
if mess.find('луны') != -1 or mess.find('луна') != -1:
    if mess.find('до') != -1:
        print('До Луны 384 400 км')
        talk('380000 км')

if mess.find('солнца') != -1 or mess.find('солнце') != -1:
    if mess.find('до') != -1:
        print('До Солнца 149 600 000 км')
        talk('150000000 км')

if mess.find('марса') != -1 or mess.find('марс') != -1:
    if mess.find('до') != -1:
        print('До Марса 225 000 000 км')
        talk('225000000 км')

if mess.find('юпитера') != -1 or mess.find('юпитер') != -1:
    if mess.find('до') != -1:
        print('До Юпитера 778 547 200 км')
        talk('770000000 км')

if mess.find('венеры') != -1 or mess.find('венера') != -1:
    if mess.find('до') != -1:
        print('До Венеры 149 500 000 км')
        talk('150000000 км')

if mess.find('меркурия') != -1 or mess.find('меркурий') != -1:
    if mess.find('до') != -1:
        print('До Меркурия 149 500 000 км')
        talk('150000000 км')

if mess.find('сатурна') != -1 or mess.find('сатурн') != -1:
    if mess.find('до') != -1:
        print('До Сатурна 128 000 000 км')
        talk('128000000 км')

if mess.find('нептуна') != -1 or mess.find('нептун') != -1:
    if mess.find('до') != -1:
        print('До Нептуна 4 450 000 000 км')
        talk('4500000000 км')

if mess.find('урана') != -1 or mess.find('уран') != -1:
    if mess.find('до') != -1:
        print('До Урана 2 875 000 000 км')
        talk('2900000000 км')

if mess.find('плутона') != -1 or mess.find('плутон') != -1:
    if mess.find('до') != -1:
        print('До Плутона 5 700 000 000 км')
        talk('5700000000 км')

if mess.find('бетельгейзе') != -1 or mess.find('бетельгейза') != -1:
    if mess.find('до') != -1:
        print('До Бетельгейзе 693 419 955 373.2749 км')
        talk('700000000000 км')

if mess.find('земли') != -1 or mess.find('земля') != -1:
    if mess.find('до') != -1:
        print('Это шутка?')
        talk('Сэр. Я не знаю')
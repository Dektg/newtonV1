# -*- coding: utf-8 -*-
from datetime import date
from os import system
from TALK import talk

if date.today().month == 1:
    date_month = 'Января'
if date.today().month == 2:
    date_month = 'Февраля'
if date.today().month == 3:
    date_month = 'Марта'
if date.today().month == 4:
    date_month = 'Апреля'
if date.today().month == 5:
    date_month = 'Мая'
if date.today().month == 6:
    date_month = 'Июня'
if date.today().month == 7:
    date_month = 'Июля'
if date.today().month == 8:
    date_month = 'Августа'
if date.today().month == 9:
    date_month = 'Сентября'
if date.today().month == 10:
    date_month = 'Октября'
if date.today().month == 11:
    date_month = 'Ноября'
if date.today().month == 12:
    date_month = 'Декабря'
print(date.today().day, date_month, date.today().year, 'год')
talk(str(date.today().day) + date_month)
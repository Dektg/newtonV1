# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

import time, os

from TALK import talk

t = int((time.ctime(time.time()))[11:-11])

url = 'https://weather.rambler.ru/vo-vladivostoke/today/'
list =[]
sourse = requests.get(url)
main_text = sourse.text

soup = BeautifulSoup(main_text, features='lxml')

table = soup.findAll('span', {'class': '_3ImX'})
for i in table:
    list.append(i.text)

if 6 <= t <= 8:
    weater = list[1]
elif 9 <= t <= 17:
    weater = list[2]
elif 18 <= t <= 21:
    weater = list[3]
else:
    weater = list[0]
if weater[0] == '-':
    minus = ' минус '
else:
    minus = ''
print('На улице ' + weater)
talk('Сэр, температура воздуха,' + minus + weater[1:-1] + ' градусов по цельсию.')


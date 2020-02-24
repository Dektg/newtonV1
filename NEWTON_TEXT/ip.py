import requests
from bs4 import BeautifulSoup

url = 'https://yandex.ru/internet/'

sourse = requests.get(url)

main_text = sourse.text

soup = BeautifulSoup(main_text, features='lxml')

li = soup.find('li', class_='parameter-wrapper general-info__parameter')
li = li.text[10:]
print('IP: ',li)

city = soup.find('div', class_='location-renderer__value')
city = city.text
print(city)

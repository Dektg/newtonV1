import requests
from bs4 import BeautifulSoup
url = 'https://primpogoda.ru/weather/triozere/.more'
sourse = requests.get(url)
main_text = sourse.text

soup = BeautifulSoup(main_text, features='lxml')
table = soup.find()
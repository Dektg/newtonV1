import requests
from bs4 import BeautifulSoup

url = 'https://minfin.com.ua/currency/nbu/'

sourse = requests.get(url)
main_text = sourse.text

soup = BeautifulSoup(main_text, features='lxml')

table = soup.find('table', {'class': 'table-auto mfm-responsive-table mfm-collapse-tr mfm-table mfcur-table-lg mfcur-table-lg-nbu'})
tr = table.find('div', {'class' : 'data-title responsive-show mfm-text-nowrap mfm-text-left'})
tr = (tr.text)[1:7]
print(tr)

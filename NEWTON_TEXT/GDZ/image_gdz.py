import requests

url = 'https://gdz.ru/attachments/images/tasks/000/005/962/0000/5d9aeafe2d157.png?d=0&s=q50Q4LO32H5ZgOqroDovuA'

r = requests.get(url, stream=True)

with open('../AI/power.txt', 'bw') as f:
    for chunk in r.iter_content(8192):
        f.write(chunk)
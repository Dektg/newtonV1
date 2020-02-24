import os, requests, html
lst = input(': ')
print(lst)
print(len(lst))
if lst == 'новости':
    test = ""
    for i in range(1, len(lst)):
        test = test + " " + str(lst[i])
        r = requests.get('https://news.yandex.ru/yandsearch?text={}&rpt=nnews2&grhow=clutop&rel=rel'.format(test)).text
        parser = html.fromstring(r)
        news = ""
        for i in range(5):
            try:
                elem = parser.cssselect('a[class="link link_theme_normal title__link i-bem"]')[i]
                print(elem.get('title'))
                news = news + elem.get('title') + "\n\n"
                #print(elem.get('href'))
            except:
                print("\nВсего " + str(i) + " новостей")
                break
        os.system("echo '{}' | RHVoice-test -p aleksandr".format(news))
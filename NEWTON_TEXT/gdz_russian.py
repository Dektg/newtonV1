# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
mess_lesson = input('Введите предмет: ').lower()

hack_text = '         ****  *****  *   *  ****    **   ***    *****  *   *  *****\n\
        *      *   *  *   *  *   *   **   *  *   *   *  *   *  *\n\
        *      *   *  *   *  *   *        *   *  *   *  **  *  *\n\
         ***   *   *  *   *  ****         *   *  *   *  * * *  ***\n\
            *  *   *  *   *  *            *   *  *   *  *  **  *\n\
            *  *   *  *   *  *       **   *  *   *   *  *   *  *\n\
        ****   *****  *****  *       **   ***    *****  *   *  *****\n'

if mess_lesson.find('русск') != -1:
    nom = input('Номер: ')
    url = 'https://gdz.ru/class-7/russkii_yazik/razumovskaja-lvova-7/' + nom + '-nom/'
    print(url, '\n')
    sourse = requests.get(url)
    main_text = sourse.text

    soup = BeautifulSoup(main_text, features='lxml')
    print(hack_text)
    table = soup.findAll('div', {'class': 'with-overtask'})
    index = 0
    for i in table:
        tr = str(table[index].findAll('img')).split('src="')[1].split('"')[0].split('amp;')
        tr = 'https:' + str(tr[0]) + str(tr[1])
        index += 1
        print(tr)

if mess_lesson.find('англ') != -1 and mess_lesson.find('язык') != -1:
    if mess_lesson.find('тетра') != -1:
        s = input('Страница: ')
        url = 'https://gdz.ru/class-7/english/workbook-spotlight-7/' + s + '-s/'
        print(url, '\n')
        sourse = requests.get(url)
        main_text = sourse.text

        soup = BeautifulSoup(main_text, features='lxml')
        print(hack_text)
        table = soup.findAll('div', {'class': 'with-overtask'})
        index = 0
        for i in table:
            tr = str(table[index].findAll('img')).split('src="')[1].split('"')[0].split('amp;')
            tr = 'https:' + str(tr[0]) + str(tr[1])
            index += 1
            print(tr)
    else:
        s = input('Страница: ')
        url = 'https://gdz.ru/class-7/english/reshebnik-angliyskiy-v-fokuse-vaulina-yu-e/' + s + '-s/'
        print(url, '\n')
        sourse = requests.get(url)
        main_text = sourse.text

        soup = BeautifulSoup(main_text, features='lxml')
        print(hack_text)
        table = soup.findAll('div', {'class': 'with-overtask'})
        index = 0
        for i in table:
            tr = str(table[index].findAll('img')).split('src="')[1].split('"')[0].split('amp;')
            tr = 'https:' + str(tr[0]) + str(tr[1])
            index += 1
            print(tr)

if mess_lesson.find('алгебр') != -1:
    if mess_lesson.find('дидакти') != -1:
        job = input('Самостоятельная (1); Контрольная (2): ').lower()
        url = ''
        if job == '1' or job == 'сам' or job == '':
            variant = input('Введите вариант(1, 2): ').lower()

            if variant == '1' or variant == '' or variant == 'один':
                k_variant = '1'
                independent_work = input('Самостоятельная работа номер: ')

            elif variant == '2' or variant == 'два':
                k_variant = '2'
                independent_work = input('Самостоятельная работа номер: ')
            nom = input('Номер: ')
            url = 'https://gdz.ru/class-7/algebra/zvavich-kuznecova-15/' + k_variant + '-' + independent_work + '-independ-' + nom + '/'
        if job == '2' or job == 'контр' or job == 'два':
            kontr_variant = input('Введите название к/р(4a, 4): ').lower()
            if kontr_variant == '1':
                k_kontr_variant = '1'
            elif kontr_variant == '1a' or kontr_variant == '1а':
                k_kontr_variant = '2'
            elif kontr_variant == '2':
                k_kontr_variant = '3'
            elif kontr_variant == '2a' or kontr_variant == '2а':
                k_kontr_variant = '4'
            elif kontr_variant == '3':
                k_kontr_variant = '5'
            elif kontr_variant == '3a' or kontr_variant == '3а':
                k_kontr_variant = '6'
            elif kontr_variant == '4':
                k_kontr_variant = "7"
            elif kontr_variant == '4a' or kontr_variant == '4а':
                k_kontr_variant = "8"
            elif kontr_variant == '5':
                k_kontr_variant = '9'
            elif kontr_variant == '5a' or kontr_variant == '5а':
                k_kontr_variant = "10"
            else:
                k_kontr_variant = kontr_variant
            variant = input('Введите вариант: ').lower()
            if variant == '':
                variant = '1'
            nom = input('Номер: ')
            url = 'https://gdz.ru/class-7/algebra/zvavich-kuznecova-15/' + k_kontr_variant + '-' + variant + '-kontrol-' + nom + '/'

        print(url, '\n')
        sourse = requests.get(url)
        main_text = sourse.text

        soup = BeautifulSoup(main_text, features='lxml')
        print(hack_text)
        table = soup.findAll('div', {'class': 'with-overtask'})
        index = 0
        for i in table:
            tr = str(table[index].findAll('img')).split('src="')[1].split('"')[0].split('amp;')
            tr = 'https:' + str(tr[0]) + str(tr[1])
            index += 1
            print(tr)
    else:
        nom = input('Номер: ')
        url = 'https://gdz.ru/class-7/algebra/makarichev-18/' + nom + '-nom/'
        print(url, '\n')
        sourse = requests.get(url)
        main_text = sourse.text

        soup = BeautifulSoup(main_text, features='lxml')
        print(hack_text)
        table = soup.findAll('div', {'class': 'with-overtask'})
        index = 0
        for i in table:
            tr = str(table[index].findAll('img')).split('src="')[1].split('"')[0].split('amp;')
            tr = 'https:' + str(tr[0]) + str(tr[1])
            index += 1
            print(tr)

if mess_lesson.find('геомет') != -1:
    if mess_lesson.find('дидакт') != -1:
        nom = input('Номер: ')
        url = 'https://gdz.ru/class-7/geometria/reshebnik-rabochaya-tetrad-k-uchebniku-geometriya-7-9-atanasyana-l-s/' + nom + '-nom/'
        print(url, '\n')
        sourse = requests.get(url)
        main_text = sourse.text

        soup = BeautifulSoup(main_text, features='lxml')
        print(hack_text)
        table = soup.findAll('div', {'class': 'with-overtask'})
        index = 0
        for i in table:
            tr = str(table[index].findAll('img')).split('src="')[1].split('"')[0].split('amp;')
            tr = 'https:' + str(tr[0]) + str(tr[1])
            index += 1
            print(tr)
    else:
        nom = input('Номер: ')
        url = 'https://gdz.ru/class-7/geometria/atanasyan-7-9/' + nom + '-nom/'
        print(url, '\n')
        sourse = requests.get(url)
        main_text = sourse.text

        soup = BeautifulSoup(main_text, features='lxml')
        print(hack_text)
        table = soup.findAll('div', {'class': 'with-overtask'})
        index = 0
        for i in table:
            tr = str(table[index].findAll('img')).split('src="')[1].split('"')[0].split('amp;')
            tr = 'https:' + str(tr[0]) + str(tr[1])
            index += 1
            print(tr)

if mess_lesson.find('истори') != -1:
    if mess_lesson.find('тетра') != -1:
        job = input('§(1); Итоги главы(2): ').lower()
        if job == '' or job == '1' or job == "один":
            paragraph = input('§: ')
            if paragraph == '6':
                paragraph = '5'
            if paragraph == '2':
                paragraph = '1'
            if paragraph == '9':
                paragraph = '8'
            if paragraph == '22':
                paragraph = '21'
            if paragraph == '25':
                paragraph = '24'
            url = 'https://gdz.ru/class-7/istoriya/klokov-tetrad/' + paragraph + '-item/'
        else:
            nom = input('Введите номер главы: ')
            url = 'https://gdz.ru/class-7/istoriya/klokov-tetrad/' + nom + '-ichapter/'
        print(url, '\n')
        sourse = requests.get(url)
        main_text = sourse.text

        soup = BeautifulSoup(main_text, features='lxml')
        print(hack_text)
        table = soup.findAll('div', {'class': 'with-overtask'})
        index = 0
        for i in table:
            tr = str(table[index].findAll('img')).split('src="')[1].split('"')[0].split('amp;')
            tr = 'https:' + str(tr[0]) + str(tr[1])
            index += 1
            print(tr)
    else:
        job = input('§(1); Итоги главы(2): ').lower()
        if job == '' or job == '1' or job == "один":
            paragraph = input('§: ')
            if paragraph == '6':
                paragraph = '5'
            if paragraph == '2':
                paragraph = '1'
            if paragraph == '9':
                paragraph = '8'
            if paragraph == '22':
                paragraph = '21'
            if paragraph == '25':
                paragraph = '24'
            url = 'https://gdz.ru/class-7/istoriya/andreev/' + paragraph + '-item/'
        else:
            nom = input('Введите номер главы: ')
            url = 'https://gdz.ru/class-7/istoriya/andreev/' + nom + '-ichapter/'
        print(url, '\n')
        sourse = requests.get(url)
        main_text = sourse.text

        soup = BeautifulSoup(main_text, features='lxml')
        print(hack_text)
        table = soup.findAll('div', {'class': 'with-overtask'})
        index = 0
        for i in table:
            tr = str(table[index].findAll('img')).split('src="')[1].split('"')[0].split('amp;')
            tr = 'https:' + str(tr[0]) + str(tr[1])
            index += 1
            print(tr)

if mess_lesson.find('хими') != -1:
    paragraph = input('Введите параграф: ')
    nom = input('Номер: ')
    url = 'https://gdz.ru/class-7/himiya/gabrielyan-vvodnij-kurs/' + paragraph + '-quest-' + nom + '/'
    print(url, '\n')
    sourse = requests.get(url)
    main_text = sourse.text

    soup = BeautifulSoup(main_text, features='lxml')
    print(hack_text)
    table = soup.findAll('div', {'class': 'with-overtask'})
    index = 0
    for i in table:
        tr = str(table[index].findAll('img')).split('src="')[1].split('"')[0].split('amp;')
        tr = 'https:' + str(tr[0]) + str(tr[1])
        index += 1
        print(tr)

if mess_lesson.find('литерат') != -1:
    s = input('Страница: ')
    if s == '5':
        s = '4'
    elif s == '51':
        s = '50'
    elif s == '76':
        s = '75'
    elif s == '170':
        s = '169'
    elif s == '192':
        s = '191'
    url = 'https://gdz.ru/class-7/literatura/merkin/1-prt-' + s + '/'
    print(url, '\n')
    sourse = requests.get(url)
    main_text = sourse.text

    soup = BeautifulSoup(main_text, features='lxml')
    table = soup.findAll('div', {'class': 'with-overtask'})
    index = 0
    for i in table:
        tr = str(table[index].findAll('img')).split('src="')[1].split('"')[0].split('amp;')
        tr = 'https:' + str(tr[0]) + str(tr[1])
        index += 1
        if tr != None:
            print(hack_text)
            print(tr)
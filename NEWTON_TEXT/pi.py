from math import sqrt
pi = (3 * (2**8)) * sqrt(2 - sqrt(2 + sqrt(2 + sqrt(2 + sqrt(2 + sqrt(2 + sqrt(2 + sqrt(2 + sqrt(2+1)))))))))
mess = input(': ').lower()
if mess.find('семен') != -1 or mess.find('семён') != -1:
    print('Семён Куликов:', end=' ')
    _phone = '79147194077'
elif mess.find('марьян') != -1:
    print('Марьяна Сидоренко:', end=' ')
    _phone = '79841505820'
elif mess.find('вику') != -1 or mess.find('вика') != -1:
    print('Вика Гринькова:', end=' ')
    _phone = '79677543694'
elif mess.find('глеб') != -1:
    fam = input("Гречушкин(1) или Голиков(2)").lower()
    if fam == '' or fam.find('греч') != -1 or fam == '1':
        print('Глеб Гречушкин:', end=' ')
        _phone = '79084488885'
    else:
        print('Глеб Голиков:', end=' ')
        _phone = '79940126087'
elif mess.find('денис') != -1:
    print('Денис До:', end=' ')
    _phone = '79841461606'
elif mess.find('диму') != -1 or mess.find('дима') != -1:
    print('Дима Лобовской:', end=' ')
    _phone = '79025246745'
elif mess.find('егор') != -1:
    print('Егор Панарин:', end=' ')
    _phone = '79532112364'
elif mess.find('лешу') != -1 or mess.find('лёшу') != -1 or \
    mess.find('леша') != -1 or mess.find('лёша') != -1:
    fam = input("Каптенор(1) или Еремеев(2) или Краснопеев(3)").lower()
    if fam == '' or fam.find('каптен') != -1 or fam == '1':
        print('Лёша Каптенор:', end=' ')
        _phone = '79644493025'
    elif fam == '2' or fam.find('ереме') != -1:
        print('Лёша Еремеев:', end=' ')
        _phone = '79147298968'
    else:
        print('Лёша Краснопеев:', end=' ')
        _phone = '79149626665'
elif mess.find('данил') != -1:
    print('Данил Зяблицкий:', end=' ')
    _phone = '79149737742'
elif mess.find('кристин') != -1:
    print('Кристина Рассказова:', end=' ')
    _phone = '79243399223'
elif mess.find('аня') != -1 or mess.find('аню') != -1 or mess.find('анну') != -1:
    fam = input("Лударева(1) или Вычужанина(2)").lower()
    if fam == '' or fam.find('луд') != -1 or fam == '1':
        print('Аня Лударева:', end=' ')
        _phone = '79662744517'
    else:
        print('Аня Вычужанина:', end=' ')
        _phone = '79673860557'
elif mess.find('наст') != -1 or mess.find('настю') != -1:
    print('Настя Дуровина:', end=' ')
    _phone = '79149784708'
elif mess.find('петя') != -1 or mess.find('петю') != -1:
    print('Петя Левченко:', end=' ')
    _phone = '79143227561'
elif mess.find('гошу') != -1 or mess.find('гоша') != -1:
    print('Гоша Савинов:', end=' ')
    _phone = '79146864725'
elif mess.find('дашу') != -1 or mess.find('даша') != -1:
    print('Даша Мосолова:', end=' ')
    _phone = '79242454191'
elif mess.find('соню') != -1 or mess.find('соня') != -1:
    print('Соня Киктенко:', end=' ')
    _phone = '79644471504'
elif mess.find('мишу') != -1 or 'миша' in mess:
#elif mess.find('мишу') != -1 or mess.find('миша') != -1:
    print('Миша Стручаев :', end=' ')
    _phone = '79520840008'
elif mess.find('лизу') != -1 or mess.find('лиза') != -1:
    print('Лиза Толмачёва:', end=' ')
    _phone = '79146691936'
elif mess.find('серого') != -1 or mess.find('серый') != -1 or mess.find('сергея') != -1 or mess.find('сергей') != -1:
    print('Сергей Транковский:', end=' ')
    _phone = '79662871237'
print(_phone)
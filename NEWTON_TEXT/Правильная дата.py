print('Привет, я Ньютон. В этой программе я могу\n\
сказать, правильна ли твоя дата.')
day = input("Введите ваш день: ")
day = int(day)
month = input("Введите ваш месяц: ")
month = int(month)
year = input('Введите ваш год: ')
year = int(year)

info = [day, month, year]


def Day():
    # Январь
    if info[1] == 1:
        if 1 <= day <= 31:
            print("Правильно")
        else:
            print("Неверный день, в Январе 31 день")

    # Февраль
    if info[1] == 2:
        if year % 400 == 0:
            if 1 <= day <= 29:
                print("Правильно")
        else:
            if year % 4 == 0 and year % 100 != 0:
                if 1 <= day <= 29:
                    print("Правильно")
                else:
                    print("Неверный день, в Феврале 29 дней")
            else:
                if 1 <= day <= 28:
                    print("Правильно")
                else:
                    print("Неверный день, в Феврале 28 дней")

    # март
    if info[1] == 3:
        if 1 <= day <= 31:
            print("Правильно")
        else:
            print("Неверный день, в Марте 31 день")

    # апрель
    if info[1] == 4:
        if 1 <= day <= 30:
            print("Правильно")
        else:
            print("Неверный день, в Апреле 30 дней")

    # май
    if info[1] == 5:
        if 1 <= day <= 29:
            print("Правильно")
        else:
            print("Неверный день, в Мае 29 дней")

    # Июнь
    if info[1] == 6:
        if 1 <= day <= 30:
            print("Правильно")
        else:
            print("Неверный день, в Июне 30 дней")
    # Июль
    if info[1] == 7:
        if 1 <= day <= 31:
            print("Правильно")
        else:
            print("Неверный день, в Июле 31 день")
    # Август
    if info[1] == 8:
        if 1 <= day <= 31:
            print("Правильно")
        else:
            print("Неверный день, в Августе 31 день")
    # Сентябрь
    if info[1] == 9:
        if 1 <= day <= 30:
            print("Правильно")
        else:
            print("Неверный день, в Сентябре 30 дней")
    # Октябрь
    if info[1] == 10:
        if 1 <= day <= 30:
            print("Правильно")
        else:
            print("Неверный день, в Октябре 30 дней")
    # Ноябрь
    if info[1] == 11:
        if 1 <= day <= 30:
            print("Правильно")
        else:
            print("Неверный день, в Ноябре 30 дней")
    # Декабрь
    if info[1] == 12:
        if 1 <= day <= 31:
            print("Правильно")
        else:
            print("Неверный день, в Декабре 31 день")
    if info[1] > 12:
        print('Неверный месяц, их 12')


Day()

print('Привет, я Ньютон. В этой программе я могу рассказать вам,\n\
к какому сезону относится твой месяц.')
month = input('Напиши номер мясяца: ')
month = int(month)


def seasons():
    if month == 12 or month == 1 or month == 2:
        print("Winter - Зима")
    if 3 <= month <= 5:
        print("Spring - Вестна")
    if 6 <= month <= 8:
        print("Summer - Лето")
    if 9 <= month <= 11:
        print("Autumn - Осень")


seasons()

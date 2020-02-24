print('Привет, я Ньютон. В этой программе я могу\n\
рассчитать твой вклад в банк.')
past_years = int(input("Сколько лет назад ты положил деньги в Банк: "))
next_years = int(input("На сколько лет вперед ты хочешь узнать свой доход: "))
contribution = int(input("Сколько денег вы положили с самого начала: "))
percent = int(input('Сколько процентов годовых: '))
sum_years = past_years + next_years
year = 1


def Bank(year):
    percent_contribution = (contribution * percent) / 100
    money = percent_contribution + contribution
    for i in range(sum_years):
        print(year, ". ", money, sep="")
        money += (money * percent) / 100
        year += 1


print("Вы вложили деньги на", sum_years, end="")
x = sum_years + 1
if 11 <= x <= 19:
    print(" лет")
else:
    if x % 10 == 1:
        print(" год")
    else:
        if 2 <= x % 10 <= 4:
            print(" года")
        else:
            print(" лет")
Bank(year)

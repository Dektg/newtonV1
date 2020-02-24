sys = 24
now = float(input("Сколько сейчас часов: "))
plus = float(input('Сколько прибавить: '))

print((now + plus) % sys, end='')  # TODO: am and pm
x = (now + plus) % sys + 1
if 11 <= x <= 19:
    print(" часов", end='')
else:
    if x % 10 == 1:
        print(" час", end='')
    else:
        if 2 <= x % 10 <= 4:
            print(" часа", end='')
        else:
            print(" часов", end='')

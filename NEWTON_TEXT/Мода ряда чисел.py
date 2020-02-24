from random import random
print('Привет, я Ньютон. В этой программе я могу\n\
найти моду числа из списка.')
count = int(input('Какой длинны будет список: '))

a = [int(random()*1000) for i in range(count)]
print(a)

a_set = set(a)# set - множество

most_common = None
qty_most_common = 0

for item in a_set:
    qty = a.count(item)
    if qty > qty_most_common:
        qty_most_common = qty
        most_common = item

print(most_common, 'встречалась', qty, end='')
x = qty
if x == 1:
    print(' раз')
    exit(0)
x = x + 1
if 11 <= x <= 19:
    print(" раз")
else:
    if x % 10 == 1:
        print(" раз")
    else:
        if 2 <= x % 10 <= 4:
            print(" раза")
        else:
            print(" раз")


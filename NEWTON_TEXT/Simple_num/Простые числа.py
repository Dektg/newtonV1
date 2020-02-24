print('Привет, я Ньютон. В этой программе я могу\n\
найти все простые числа из ряда чисел.')
count = int(input('Введите до какго числа считать: '))
f = open('Simple_Nums.txt', 'w')
k = 0
simples = 0
for i in range(2, count):
    for j in range(2, i):
        if i % j == 0:
            k = k + 1
    # если делителей нет, simples += 1
    if k == 0:
        simples += 1
        f.write(str(i)+'\n')
        print(i)
    else:
        k = 0
print("Нашёл", simples, end='')
x = simples + 1
if 11 <= x <= 19:
    print(" простых чисел")
else:
    if x % 10 == 1:
        print(" простое число")
    else:
        if 2 <= x % 10 <= 4:
            print(" простых числа")
        else:
            print(" простых числа")

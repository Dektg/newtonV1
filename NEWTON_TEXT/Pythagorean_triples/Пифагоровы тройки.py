print('Привет, я Ньютон. В этой программе я могу\n\
написать в Nums.txt все Пифагоравы тройки в нужное кол-во раз.')
f = open('Nums.txt', 'w')
const = int(input('Введите кол-во раз: '))
m = 1
for i in range(const):
    a = (2 * m) + 1
    b = (2 * m) * (m + 1)
    с = 2 * (m ** 2) + a
    m += 1
    if a ** 2 + b ** 2 == с ** 2:
        f.write(str([a, b, с]) + '\n')
        print(a, b, с)
f.close()

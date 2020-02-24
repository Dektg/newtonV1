print('Привет, я Ньютон. В этой программе я могу\n\
сложить все написанные вами цифры.')
def summa(a):
    a = a.split()
    b = []
    for i in a:
        b.append(int(i))
    return sum(b)


s = 0
while 1:
    a = input()
    if a == '_': break
    s += summa(a)
    print('Cумма =', s)

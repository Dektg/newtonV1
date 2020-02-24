print('Привет, я Ньютон. В этой программе я могу\n\
найти объем тела, массу или плотность.\n\
Обозначение операций:\n\
1. Объём = V\n\
2. Плотность = p\n\
3. Масса = m')
choice = input('Что вы хотите узнать: ')
if choice == 'V':
    m = int(input('m = '))
    p = int(input('p = '))
    print('V = m / p\nV =', m / p)
if choice == 'm':
    V = int(input('V = '))
    p = int(input('p = '))
    print('m = p * V\nm =', p * V)
if choice == 'p':
    V = int(input('V = '))
    m = int(input('m = '))
    print('p = m / V\np =', m / V)

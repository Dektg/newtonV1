print('Привет, я Ньютон. В этой программе я могу\n\
перевести число в другую систему счисления.')
namber = int(input('Введите число: '))
k = int(input('В какую систему счисления перевести: '))


def dec_to_base(N, base):
    if not hasattr(dec_to_base, 'table'):
        dec_to_base.table = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    x, y = divmod(N, base)
    return dec_to_base(x, base) + dec_to_base.table[y] if x else dec_to_base.table[y]


print(dec_to_base(namber, k))

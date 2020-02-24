mess = int(input())
if mess % 10 == 1 and mess % 100 != 11:
    print(str(mess) + ' рубль')
elif mess % 10 in [2, 3, 4] and mess % 100 not in [12, 13, 14]:
    print(str(mess) + ' рубля')
elif mess % 10 == 0 or mess % 10 in [5, 6, 7, 8, 9] or mess % 100 in [11, 12, 13, 14]:
    print(str(mess) + ' рублей')

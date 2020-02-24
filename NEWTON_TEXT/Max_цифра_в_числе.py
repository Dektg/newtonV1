num = float(input('Введите ваше число: '))
strNum = str(num)

maxDigit = -1

for i in range(len(strNum)):
    if strNum[i] == '.':
        continue
    elif maxDigit < int(strNum[i]):
        maxDigit = int(strNum[i])

print('Цыфра:', maxDigit)
################

summ = 0
nums = []
while True:
    num = input('Число: ')
    if num == '':
        break
    num = int(num)
    nums.append(num)
    summ = summ + num
print(round(summ/len(nums),2),sep='')

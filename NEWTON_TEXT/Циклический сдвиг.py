print('Привет, я Ньютон. В этой программе я могу\n\
сделать циклический сдвиг.')
def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())


nums = input('Напишите числовой ряд через пробел:').split(' ')
print(nums)
while True:
    shift(nums, int(input('На сколько единиц будет сдвинут числовой ряд: ')))
    print(nums)

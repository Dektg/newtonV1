print('Привет, я Ньютон. В этой программе я могу сказать вам\n\
идентификатор элемента, который вы ищете в списке.\n\
Просто напишите мне ваше число.')
from random import random
N = 20
array = []
for i in range(N):
    array.append(int(random()*100))
array.sort()
print(array)

number = int(input())

low = 0
high = N-1
while low <= high:
    mid = (low + high) // 2
    if number < array[mid]:
        high = mid - 1
    elif number > array[mid]:
        low = mid + 1
    else:
        print("Index =", mid)
        break
else:
    print("Не ясно")
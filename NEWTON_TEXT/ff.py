a = [1,2]
count = int(input('Введите до какго числа считать: '))
k = 0
ds = 0
for i in range(348908, count):
    for j in range(2, i):
        if i % j == 0:
            k = k + 1

    if k == 0:
        a.append(i)
        print(i, ' =-= ', end='')
        print(a[a.index(i)] - a[a.index(i) -1])
    else:
        k = 0

for elem in range(len(a)):
    print(a[elem+1]-a[elem])
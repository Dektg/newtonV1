from random import random
print('Привет, я Ньютон. В этой программе я могу\n\
найти в матрице любое число, которое вы хотите.')
N = 10
M = 15
matrix = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(int(random()*70)+10)
    print(row)
    matrix.append(row)

item = int(input("Число из матрицы: "))

print("Строка: ", end=" ")#TODO: Сделать для каждого найденного цисла отделные координаты
for i in range(N):
    if item in matrix[i]:
        print(i + 1, end=" ")
print()

print("Столбец:", end=" ")
for j in range(M):
    for i in range(N):
        if matrix[i][j] == item :
            print(j + 1, end=' ')
            break
print()
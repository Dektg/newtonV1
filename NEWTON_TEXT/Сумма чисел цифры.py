print('Привет, я Ньютон. В этой программе я могуn\n\
найти сумму всех цифр трехзначного числа')
namber = int(input('Введите число: '))
namber_str = list(str(namber))

print("Число =", namber_str[0] + namber_str[1] + namber_str[2])

a = int(namber_str[0])
b = int(namber_str[1])
c = int(namber_str[2])

print("Сумма цифр числа =", a + b + c)

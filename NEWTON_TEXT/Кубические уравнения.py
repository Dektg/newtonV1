
print('ax³ + 3bx² + 3cx + d = 0')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
d = int(input('d: '))

p = (c/a) - (b**2/a**2)

q = -3 *((b*c)/a**2) + ((2 * b**3)/a**3) + d/a

y = (-q/2 + (((q/2)**2 + p**3)**(1/3)))**(1/3) - p / (-q/2 + (((q/2)**2 + p**3)**(1/3)))**(1/3)

x = y - (b/a)
print(x)
print('|!e * x + d!+ a|+ b = c')
c = int(input('c = '))
if c < 0:
    print('У уранения нет корней\nx ∈ Ø')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
d = int(input('d = '))
e = int(input('e = '))

x1 = (((c - b) - a) - d) / e
x2 = -(((c - b) - a) - d) / e
print('x₁ =',x1, '\nx₂ =',x2)
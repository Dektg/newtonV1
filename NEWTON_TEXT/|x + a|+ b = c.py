
print('|x + a|+ b = c')
c = int(input('c = '))
if c < 0:
    print('У уранения нет корней\nx ∈ Ø')
a = int(input('a = '))
b = int(input('b = '))
if a == 0 and b == 0:
    if c >= 0:
        print('x₁ =', c, '\nx₂ =', -c)
if c != 0 and b != 0 and a != 0:
    x1 = (c - b) - a
    x2 = -(c - b) - a
    print('x₁ =',x1, '\nx₂ =',x2)





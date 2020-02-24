angle_a = int(input('Введите первый угол: '))
angle_b = int(input('Введите второй угол: '))
if angle_a == 60 and angle_b == 60:
    print('\nТреугольник равносторонний: 60 60 60')
    exit(0)
angle_с = 180 - (angle_a + angle_b)
print('Третий угол = ',angle_с,'\n\
 Δ = ',angle_a,' + ',angle_b,' + ',angle_с,' = 180°',sep='')
if angle_a == angle_b or angle_a == angle_с or angle_с == angle_b:
    print('\nТреугольник равнобедренный: ', end='')
if angle_a == angle_b:
    print(angle_a, 'и', angle_b)
if angle_a == angle_с:
    print(angle_a, 'и', angle_с)
if angle_b == angle_с:
    print(angle_b, 'и', angle_с)


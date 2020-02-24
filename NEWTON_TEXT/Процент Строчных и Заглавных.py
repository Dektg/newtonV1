print('Привет, я Ньютон. В этой программе я могу рассчитать\n\
процент строчных и заглавных букв в тексте.')
string = input("Введите текст: ")

length = len(string)
let_s = let_b = 0
for i in string:
    if 'a' <= i <= 'z':
        let_s += 1
    elif 'A' <= i <= 'Z':
        let_b += 1

print("Строчные буквы =", round(let_s / length * 100), '%')
print("Заглавные буквы =", round(let_b / length * 100), '%')

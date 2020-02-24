print('Привет, я Ньютон. В этой программе я могу\n\
найти самое длинное слово из текста')
string = input('Введите текст: ')

listWords = string.split()

idLongestWord = 0

for i in range(1, len(listWords)):
    if len(listWords[idLongestWord]) < len(listWords[i]):
        idLongestWord = i

print(listWords[idLongestWord])
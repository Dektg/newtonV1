print('Привет, я Ньютон. В этой программе я могу\n\
очистить текст от всех знаков препинания.')
string = input('Введите ваш текст: ')

punctuation = ['`','"', "'", ':', ';', '!', '?', '(', ')','[',']','-']

wordList = string.split()

i = 0
for word in wordList:
    if word[-1] in punctuation:
        wordList[i] = word[:-1]
        word = wordList[i]
    if word[0] in punctuation:
        wordList[i] = word[1:]
    i += 1
for l in wordList:
    print(l, end=' ')
print()
print(wordList)

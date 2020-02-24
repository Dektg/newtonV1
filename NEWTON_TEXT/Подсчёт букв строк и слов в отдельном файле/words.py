import sys

print('Привет, я Ньютон. В этой программе я могу сказать количество\n\
строк, букв и слов из текста, записанного в файле text.txt.')

fname = sys.argv[1]
lines = 0
words = 0
letters = 0

for line in open(fname):
    lines += 1
    letters += len(line)

    pos = 'out'
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'

print("Строк:", lines)
print("Слов:", words)
print("Букв:", letters)
#python3 words.py text.txt
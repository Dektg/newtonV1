# -*- coding: utf-8 -*-
from A_command import mess
import os
import wikipedia
from translate import Translator

from TALK import talk

list_words = []
clean_mess = []
mess_split = mess.split(' ')
for a in mess_split:
    if a != 'покажи' and a != 'расскажи' and a != 'скажи' and a != 'про' and a != 'найди' and a != 'значение' \
        and a != 'смысл' and a != 'что' and a != 'значит' and a != 'означает' and a != 'такое' and a != 'в' \
        and a != 'википедии' and a != 'выражения' and a != 'предложения' and a != 'словосочетания' and a != 'кто' \
        and a != 'такой':
        clean_mess.append(a)
print(''.join(clean_mess))
translatable_word = ' '.join(clean_mess)
translator = Translator(from_lang="russian", to_lang="english")
translatable_word = translator.translate(translatable_word)
text_ = wikipedia.summary(translatable_word, sentences=1)
print(text_)

translator = Translator(from_lang="english", to_lang="russian")
translation = translator.translate(text_)
print(translation)

translation_list = list(translation.lower())

if translation.find(')') != -1 and translation.find('(') != -1:

    for i in translation_list:
        if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' \
            or i == '8' or i == '9' or i == 'а' or i == '.' or i == ',' or i == ' ' or i == 'a' or i == 'б' \
            or i == 'в' or i == 'г' or i == 'д' or i == 'е' or i == 'ё' or i == 'ж' or i == 'з' or i == 'и' \
            or i == 'й' or i == 'к' or i == 'л' or i == 'м' or i == 'н' or i == 'о' or i == 'п' or i == 'р' \
            or i == 'с' or i == 'т' or i == 'у' or i == 'ф' or i == 'ч' or i == 'ц' or i == 'ч' or i == 'ш' \
            or i == 'щ' or i == 'ъ' or i == 'ы' or i == 'ь' or i == 'э' or i == 'ю' or i == 'я' or i == 'a' \
            or i == 'b' or i == 'c' or i == 'd' or i == 'e' or i == 'f' or i == 'g' or i == 'h' or i == 'i' \
            or i == 'j' or i == 'k' or i == 'l' or i == 'm' or i == 'n' or i == 'o' or i == 'p' or i == 'q' \
            or i == 'r' or i == 's' or i == 't' or i == 'u' or i == 'v' or i == 'w' or i == 'x' or i == 'y' \
            or i == 'z':
            list_words.append(i)

    translation = ''.join(list_words)
talk(translation)

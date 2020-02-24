def clear_text(test_str):
    ret = ''
    skip1c = 0
    skip2c = 0
    for i in test_str:
        if i == '[':
            skip1c += 1
        elif i == '(':
            skip2c += 1
        elif i == ']' and skip1c > 0:
            skip1c -= 1
        elif i == ')' and skip2c > 0:
            skip2c -= 1
        elif skip1c == 0 and skip2c == 0:
            ret += i
    return ret
x = "Михаил Васильевич Ломоносов  Васи́льевич Ломоно́сов, МПА: [mʲɪxɐˈil vɐˈsʲilʲjɪvʲɪtɕ ləmɐˈnosəf] (слушайте); 19 ноября [О.С. 8 ноября] 1711 - 15 апреля [О.С. 4] 1765) был русский и политолог писатель, который внес важный вклад в литературу, образование и науку. Среди его открытий были атмосфера Венеры и закон сохранения массы в химических реакциях."
print(x)
x = clear_text(x)
print(repr(x))

if ((mess.find('покажи') != -1 or mess.find('расскажи') != -1 or mess.find('скажи') != -1) \
    and mess.find('про') != -1) or (
        mess.find('найди') != -1 and (mess.find('значение') != -1 or mess.find('смысл') != -1 \
                                      or mess.find('выражения') != -1 or mess.find('предложения') != -1 or mess.find(
            'словосочетания') != -1)) \
        or ((mess.find('что') != -1 or mess.find('кто') != -1) and (
        mess.find('такой') != -1 or mess.find('значит') != -1 or mess.find('означает') != -1 \
        or mess.find('такое') != -1)) or (
        mess.find('в') != -1 and (mess.find('википедии') != -1 or mess.find('википедия') != -1)):
    file = open('A_command.py', 'w')
    file.write("mess = '" + mess + "'")
    file.close()
    import wiki_book

    del wiki_book
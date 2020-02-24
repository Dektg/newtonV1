# -*- coding: utf-8 -*-
slova = input('Введите слово: ').lower()
sloval = list(slova)
pole = [[ [] ]* len(slova),
        [ [] ]* len(slova),
        [ [] ]* len(slova),
        [ [] ]* len(slova),
        [ [] ]* len(slova),
        [ [] ]* len(slova),
        [ [] ]* len(slova)]
num = 0
for j in sloval:

    def Start():
        if sloval.count(j) > 1:

            if sloval.index(j) != num:

                start_search = sloval.count(j)
                return start_search
            else:
                start_search = 0
                return start_search


        else:

            start_search = 0
            return start_search

    start_search = Start()
    if j == 'a':
        pole[0][sloval.index(j, start_search)] = '   *   '
        pole[1][sloval.index(j, start_search)] = '  * *  '
        pole[2][sloval.index(j, start_search)] = ' *   * '
        pole[3][sloval.index(j, start_search)] = '*     *'
        pole[4][sloval.index(j, start_search)] = '*******'
        pole[5][sloval.index(j, start_search)] = '*     *'
        pole[6][sloval.index(j, start_search)] = '*     *'
    elif j == 'b':
        pole[0][sloval.index(j, start_search)] = '****** '
        pole[1][sloval.index(j, start_search)] = '*     *'
        pole[2][sloval.index(j, start_search)] = '*     *'
        pole[3][sloval.index(j, start_search)] = '****** '
        pole[4][sloval.index(j, start_search)] = '*     *'
        pole[5][sloval.index(j, start_search)] = '*     *'
        pole[6][sloval.index(j, start_search)] = '****** '
    elif j == 'c':
        pole[0][sloval.index(j, start_search)] = ' ***** '
        pole[1][sloval.index(j, start_search)] = '*     *'
        pole[2][sloval.index(j, start_search)] = '*      '
        pole[3][sloval.index(j, start_search)] = '*      '
        pole[4][sloval.index(j, start_search)] = '*      '
        pole[5][sloval.index(j, start_search)] = '*     *'
        pole[6][sloval.index(j, start_search)] = ' ***** '
    elif j == 'd':
        pole[0][sloval.index(j, start_search)] = '*****  '
        pole[1][sloval.index(j, start_search)] = '*    * '
        pole[2][sloval.index(j, start_search)] = '*     *'
        pole[3][sloval.index(j, start_search)] = '*     *'
        pole[4][sloval.index(j, start_search)] = '*     *'
        pole[5][sloval.index(j, start_search)] = '*    * '
        pole[6][sloval.index(j, start_search)] = '*****  '
    elif j == 'e':
        pole[0][sloval.index(j, start_search)] = '*******'
        pole[1][sloval.index(j, start_search)] = '*      '
        pole[2][sloval.index(j, start_search)] = '*      '
        pole[3][sloval.index(j, start_search)] = '*****  '
        pole[4][sloval.index(j, start_search)] = '*      '
        pole[5][sloval.index(j, start_search)] = '*      '
        pole[6][sloval.index(j, start_search)] = '*******'
    elif j == 'f':
        pole[0][sloval.index(j, start_search)] = '*******'
        pole[1][sloval.index(j, start_search)] = '*      '
        pole[2][sloval.index(j, start_search)] = '*      '
        pole[3][sloval.index(j, start_search)] = '*****  '
        pole[4][sloval.index(j, start_search)] = '*      '
        pole[5][sloval.index(j, start_search)] = '*      '
        pole[6][sloval.index(j, start_search)] = '*      '
    elif j == 'g':
        pole[0][sloval.index(j, start_search)] = ' ***** '
        pole[1][sloval.index(j, start_search)] = '*     *'
        pole[2][sloval.index(j, start_search)] = '*      '
        pole[3][sloval.index(j, start_search)] = '*      '
        pole[4][sloval.index(j, start_search)] = '*   ***'
        pole[5][sloval.index(j, start_search)] = '*     *'
        pole[6][sloval.index(j, start_search)] = '****** '
    elif j == 'h':
        pole[0][sloval.index(j, start_search)] = '*     *'
        pole[1][sloval.index(j, start_search)] = '*     *'
        pole[2][sloval.index(j, start_search)] = '*     *'
        pole[3][sloval.index(j, start_search)] = '*******'
        pole[4][sloval.index(j, start_search)] = '*     *'
        pole[5][sloval.index(j, start_search)] = '*     *'
        pole[6][sloval.index(j, start_search)] = '*     *'
    elif j == 'i':
        pole[0][sloval.index(j, start_search)] = '*******'
        pole[1][sloval.index(j, start_search)] = '   *   '
        pole[2][sloval.index(j, start_search)] = '   *   '
        pole[3][sloval.index(j, start_search)] = '   *   '
        pole[4][sloval.index(j, start_search)] = '   *   '
        pole[5][sloval.index(j, start_search)] = '   *   '
        pole[6][sloval.index(j, start_search)] = '*******'
    elif j == 'j':
        pole[0][sloval.index(j, start_search)] = ' ******'
        pole[1][sloval.index(j, start_search)] = '     * '
        pole[2][sloval.index(j, start_search)] = '     * '
        pole[3][sloval.index(j, start_search)] = '     * '
        pole[4][sloval.index(j, start_search)] = '*    * '
        pole[5][sloval.index(j, start_search)] = '*    * '
        pole[6][sloval.index(j, start_search)] = ' ***** '
    elif j == 'k':
        pole[0][sloval.index(j, start_search)] = '*     *'
        pole[1][sloval.index(j, start_search)] = '*    * '
        pole[2][sloval.index(j, start_search)] = '*   *  '
        pole[3][sloval.index(j, start_search)] = '****   '
        pole[4][sloval.index(j, start_search)] = '*   *  '
        pole[5][sloval.index(j, start_search)] = '*    * '
        pole[6][sloval.index(j, start_search)] = '*     *'
    elif j == 'l':
        pole[0][sloval.index(j, start_search)] = '*      '
        pole[1][sloval.index(j, start_search)] = '*      '
        pole[2][sloval.index(j, start_search)] = '*      '
        pole[3][sloval.index(j, start_search)] = '*      '
        pole[4][sloval.index(j, start_search)] = '*      '
        pole[5][sloval.index(j, start_search)] = '*      '
        pole[6][sloval.index(j, start_search)] = '*******'
    elif j == 'm':
        pole[0][sloval.index(j, start_search)] = '*     *'
        pole[1][sloval.index(j, start_search)] = '**   **'
        pole[2][sloval.index(j, start_search)] = '* * * *'
        pole[3][sloval.index(j, start_search)] = '*  *  *'
        pole[4][sloval.index(j, start_search)] = '*     *'
        pole[5][sloval.index(j, start_search)] = '*     *'
        pole[6][sloval.index(j, start_search)] = '*     *'
    elif j == 'n':
        pole[0][sloval.index(j, start_search)] = '*     *'
        pole[1][sloval.index(j, start_search)] = '**    *'
        pole[2][sloval.index(j, start_search)] = '* *   *'
        pole[3][sloval.index(j, start_search)] = '*  *  *'
        pole[4][sloval.index(j, start_search)] = '*   * *'
        pole[5][sloval.index(j, start_search)] = '*    **'
        pole[6][sloval.index(j, start_search)] = '*     *'

    elif j == 'o':
        pole[0][sloval.index(j, start_search)] = '*******'
        pole[1][sloval.index(j, start_search)] = '*     *'
        pole[2][sloval.index(j, start_search)] = '*     *'
        pole[3][sloval.index(j, start_search)] = '*     *'
        pole[4][sloval.index(j, start_search)] = '*     *'
        pole[5][sloval.index(j, start_search)] = '*     *'
        pole[6][sloval.index(j, start_search)] = '*******'

    elif j == 'p':
        pole[0][sloval.index(j, start_search)] = '****** '
        pole[1][sloval.index(j, start_search)] = '*     *'
        pole[2][sloval.index(j, start_search)] = '*     *'
        pole[3][sloval.index(j, start_search)] = '****** '
        pole[4][sloval.index(j, start_search)] = '*      '
        pole[5][sloval.index(j, start_search)] = '*      '
        pole[6][sloval.index(j, start_search)] = '*      '
    elif j == 'q':
        pole[0][sloval.index(j, start_search)] = '*******'
        pole[1][sloval.index(j, start_search)] = '*     *'
        pole[2][sloval.index(j, start_search)] = '*     *'
        pole[3][sloval.index(j, start_search)] = '*     *'
        pole[4][sloval.index(j, start_search)] = '*   * *'
        pole[5][sloval.index(j, start_search)] = '*******'
        pole[6][sloval.index(j, start_search)] = '     * '
    elif j == 'r':
        pole[0][sloval.index(j, start_search)] = '****** '
        pole[1][sloval.index(j, start_search)] = '*     *'
        pole[2][sloval.index(j, start_search)] = '*     *'
        pole[3][sloval.index(j, start_search)] = '****** '
        pole[4][sloval.index(j, start_search)] = '*   *  '
        pole[5][sloval.index(j, start_search)] = '*    * '
        pole[6][sloval.index(j, start_search)] = '*     *'
    elif j == 's':
        pole[0][sloval.index(j, start_search)] = ' ***** '
        pole[1][sloval.index(j, start_search)] = '*     *'
        pole[2][sloval.index(j, start_search)] = '*      '
        pole[3][sloval.index(j, start_search)] = ' ***** '
        pole[4][sloval.index(j, start_search)] = '      *'
        pole[5][sloval.index(j, start_search)] = '      *'
        pole[6][sloval.index(j, start_search)] = ' ***** '
    elif j == 't':
        pole[0][sloval.index(j, start_search)] = '*******'
        pole[1][sloval.index(j, start_search)] = '   *   '
        pole[2][sloval.index(j, start_search)] = '   *   '
        pole[3][sloval.index(j, start_search)] = '   *   '
        pole[4][sloval.index(j, start_search)] = '   *   '
        pole[5][sloval.index(j, start_search)] = '   *   '
        pole[6][sloval.index(j, start_search)] = '   *   '
    elif j == 'u':
        pole[0][sloval.index(j, start_search)] = '*     *'
        pole[1][sloval.index(j, start_search)] = '*     *'
        pole[2][sloval.index(j, start_search)] = '*     *'
        pole[3][sloval.index(j, start_search)] = '*     *'
        pole[4][sloval.index(j, start_search)] = '*     *'
        pole[5][sloval.index(j, start_search)] = '*     *'
        pole[6][sloval.index(j, start_search)] = '*******'
    elif j == 'v':
        pole[0][sloval.index(j, start_search)] = '*     *'
        pole[1][sloval.index(j, start_search)] = '*     *'
        pole[2][sloval.index(j, start_search)] = '*     *'
        pole[3][sloval.index(j, start_search)] = ' *   * '
        pole[4][sloval.index(j, start_search)] = ' *   * '
        pole[5][sloval.index(j, start_search)] = '  * *  '
        pole[6][sloval.index(j, start_search)] = '   *   '
    elif j == 'w':
        pole[0][sloval.index(j, start_search)] = '*     *'
        pole[1][sloval.index(j, start_search)] = '*  *  *'
        pole[2][sloval.index(j, start_search)] = '*  *  *'
        pole[3][sloval.index(j, start_search)] = '*  *  *'
        pole[4][sloval.index(j, start_search)] = '*  *  *'
        pole[5][sloval.index(j, start_search)] = '*  *  *'
        pole[6][sloval.index(j, start_search)] = ' ** ** '
    elif j == 'x':
        pole[0][sloval.index(j, start_search)] = '*     *'
        pole[1][sloval.index(j, start_search)] = ' *   * '
        pole[2][sloval.index(j, start_search)] = '  * *  '
        pole[3][sloval.index(j, start_search)] = '   *   '
        pole[4][sloval.index(j, start_search)] = '  * *  '
        pole[5][sloval.index(j, start_search)] = ' *   * '
        pole[6][sloval.index(j, start_search)] = '*     *'
    elif j == 'y':
        pole[0][sloval.index(j, start_search)] = '*     *'
        pole[1][sloval.index(j, start_search)] = '*     *'
        pole[2][sloval.index(j, start_search)] = ' *   * '
        pole[3][sloval.index(j, start_search)] = '  * *  '
        pole[4][sloval.index(j, start_search)] = '   *   '
        pole[5][sloval.index(j, start_search)] = '   *   '
        pole[6][sloval.index(j, start_search)] = '   *   '
    elif j == 'z':
        pole[0][sloval.index(j, start_search)] = '*******'
        pole[1][sloval.index(j, start_search)] = '     * '
        pole[2][sloval.index(j, start_search)] = '    *  '
        pole[3][sloval.index(j, start_search)] = '   *   '
        pole[4][sloval.index(j, start_search)] = '  *    '
        pole[5][sloval.index(j, start_search)] = ' *     '
        pole[6][sloval.index(j, start_search)] = '*******'
    elif j == ' ':
        pole[0][sloval.index(j, start_search)] = '   '
        pole[1][sloval.index(j, start_search)] = '   '
        pole[2][sloval.index(j, start_search)] = '   '
        pole[3][sloval.index(j, start_search)] = '   '
        pole[4][sloval.index(j, start_search)] = '   '
        pole[5][sloval.index(j, start_search)] = '   '
        pole[6][sloval.index(j, start_search)] = '   '
    elif j == '.':
        pole[0][sloval.index(j, start_search)] = '    '
        pole[1][sloval.index(j, start_search)] = '    '
        pole[2][sloval.index(j, start_search)] = '    '
        pole[3][sloval.index(j, start_search)] = '    '
        pole[4][sloval.index(j, start_search)] = '    '
        pole[5][sloval.index(j, start_search)] = ' ** '
        pole[6][sloval.index(j, start_search)] = ' ** '
    elif j == ':':
        pole[0][sloval.index(j, start_search)] = ' ** '
        pole[1][sloval.index(j, start_search)] = ' ** '
        pole[2][sloval.index(j, start_search)] = '    '
        pole[3][sloval.index(j, start_search)] = '    '
        pole[4][sloval.index(j, start_search)] = '    '
        pole[5][sloval.index(j, start_search)] = ' ** '
        pole[6][sloval.index(j, start_search)] = ' ** '
    else:
        pass
    num += 1

for i in pole:
    i = '  '.join(i)
    print(i)
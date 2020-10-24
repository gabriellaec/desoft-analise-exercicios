def apaga_repetidos(string):
    lista = []
    new = ''
    for i in range(len(string)):
        add = ''
        for x in lista:
            if string[i].upper() == x.upper():
                add = '*'
                new += add
        if add != '*':
            add = string[i]
            new += add
            lista.append(add)
    return new
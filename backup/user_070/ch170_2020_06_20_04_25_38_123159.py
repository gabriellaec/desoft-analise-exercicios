def apaga_repetidos(string):
    lista = []
    new = ''
    add = ''
    for i in range(len(string)):
        for x in lista:
            if upper(string[i]) == upper(x):
                add = '*'
                new += add
        if add != '*':
            add = string[i]
            new += add
            lista.append(add)
    return new
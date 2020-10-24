def apaga_repetidos(string):
    lista = []
    final = ''
    for x in string:
        add = x
        if x.upper() not in lista:
            lista.append(x.upper())
        else:
            add = '*'
        final += add
    return final
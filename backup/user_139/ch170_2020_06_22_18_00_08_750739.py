def apaga_repetidos (string):
    lista = []
    final = " "
    for x in string:
        if x.upper() not in lista:
            final += x
            lista.append(x.upper())
        else:
            final += '*'
    return final
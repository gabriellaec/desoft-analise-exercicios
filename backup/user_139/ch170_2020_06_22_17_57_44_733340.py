def apaga_repetidos (string):
    lista = []
    final = " "
    for x in string:
        if x not in lista or x.upper not in lista:
            final += x
            lista.append(x)
        else:
            final += '*'
    return final
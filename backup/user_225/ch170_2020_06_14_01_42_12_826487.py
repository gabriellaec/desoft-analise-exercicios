def apaga_repetidos(string):
    lista = []
    for i in string:
        if i in lista:
            lista.append('*')
        else:
            lista.append(i)
    a = ''.join(lista)
    return a
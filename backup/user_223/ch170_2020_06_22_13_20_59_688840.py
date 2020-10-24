def apaga_repetidos(string):
    separado = list(string)
    lista = []
    for c in separado:
        if c not in lista:
            lista.append(c)
        else:
            lista.append('*')
    texto = lista.join()
    return texto
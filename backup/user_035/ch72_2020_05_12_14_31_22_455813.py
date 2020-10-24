def lista_caracteres(x):
    lista = []
    i = 0
    while i < len(x):
        if x[i] in lista:
            i += 1
        else:
            lista.append(x[i])
            i += 1
    return lista
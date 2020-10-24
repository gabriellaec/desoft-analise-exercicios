def lista_caracteres(x):
    lista = []
    for e in x:
        if e not in lista:
            lista.append(e)
    return lista
            
def lista_caracteres(string):
    lista = []
    for e in string:
        if e not in lista:
            lista.append(e)
    return lista
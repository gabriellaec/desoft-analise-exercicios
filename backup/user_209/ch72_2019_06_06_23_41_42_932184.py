def lista_caracteres (string):
    lista = []
    for e in range(len(string)):
        if string[e] not in lista:
            lista.append(e)
    return lista
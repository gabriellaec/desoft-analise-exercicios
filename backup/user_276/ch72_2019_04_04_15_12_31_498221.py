def lista_caracteres(string):
    i = 0
    lista = []
    while i < len(string):
        if string[i] not in lista:
            lista.append(string[i])
        i += 1
    return lista
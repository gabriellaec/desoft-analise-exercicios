def lista_caracteres(string):
    lista = []
    for i in range(len(string)):
        if string[i] not in lista:
            lista.append(string[i])
    return lista
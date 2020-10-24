def lista_caracteres (texto):
    lista = []
    i = 0
    while i < len(texto):
        if texto[i] not in lista:
            lista.append(texto[i])
            i += 1
        else:
            i += 1
    return lista
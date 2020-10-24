def lista_caracteres (texto):
    lista = []
    for i in range(len(texto)):
        if texto[i] not in lista:
            lista.append(texto[i])
    return lista
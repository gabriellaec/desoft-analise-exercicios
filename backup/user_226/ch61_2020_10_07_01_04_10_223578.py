def filtra_positivos(lista):
    i = 0
    lista_nova = []
    while i < len(lista):
        if lista[i] > 0:
            lista_nova.append(lista[i])
        i += 1
    return lista_nova

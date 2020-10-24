def filtra_positivos(lista):
    i = 0
    lista_nova = []
    while i < len(lista):
        if lista[i] > 0:
            lista_nova.append(lista)
        else:
            lista_nova = lista_nova
        i += 1
    return lista_nova
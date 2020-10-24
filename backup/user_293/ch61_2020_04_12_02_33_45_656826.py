def filtra_positivos(lista):
    lista_pos = []
    i = 0
    while i < len(lista):
        if lista[i] > 0:
            lista_pos.append(lista[i])
        i += 1
    return lista_pos
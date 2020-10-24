def filtra_positivos(lista):
    list_pos = []
    for e in lista:
        if e > 0:
            list_pos.append(e)
    return list_pos
def filtra_positivos(lista):
    lista_pos = []
    for e in lista:
        if e > 0:
            lista_pos.append(e)
    return lista_pos
def filtra_positivos(lista):
    lista_positivos={}
    for e in lista:
        if e>=0:
            lista_positivos.append(e)
        else:
            return lista
    return lista_positivos
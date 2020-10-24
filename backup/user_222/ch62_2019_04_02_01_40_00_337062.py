def filtra_positivos(lista):
    lista_positivos={}
    y=0
    for e in lista:
        if e>=0:
            lista_positivos.append(e)
        else:
            y=e
    return lista_positivos
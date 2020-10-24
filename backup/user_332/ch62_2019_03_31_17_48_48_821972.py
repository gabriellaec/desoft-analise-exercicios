def filtra_positivos (lista):
    lista_positiva = []
    for e in lista:
        if(e > 0):
            lista_positiva.append(e)
    return(lista_positiva)
def filtra_positivos(lista):
    lista_positivos=[]
    for i in lista:
        if i > 0:
            lista_positivos.append(i)
    return lista_positivos
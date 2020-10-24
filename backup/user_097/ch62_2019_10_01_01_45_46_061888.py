def filtra_positivos(lista):
    i = 0
    lista_positivos = []
    while (i < len(lista)):
        if(lista[i]>0):
            lista_positivos.append(lista[i])
        i = i +1
    return lista_positivos
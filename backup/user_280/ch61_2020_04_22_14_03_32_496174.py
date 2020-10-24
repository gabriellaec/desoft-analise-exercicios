def filtra_positivos(lista):
    lista_positivos = []
    i=0
    while i<len(lista):
        if lista[i] > 0:
            lista_positivos.append(lista[i])
        i+=1
    return lista_positivos
    
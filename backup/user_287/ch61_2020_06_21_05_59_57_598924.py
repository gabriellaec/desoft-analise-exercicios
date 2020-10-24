def filtra_positivos(lista):
    lista = []
    lista_positv = []
    for i in lista:
        if lista[i]>0:
            lista_positv.append(lista[i])
            return lista_positv
        else:
            return lista_positv
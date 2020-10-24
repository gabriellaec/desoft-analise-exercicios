def filtra_positivos(lista):
    lista_p = []
    i = 0
    while i < len(lista):
        if lista[i] > 0:
            lista_p.append(lista[i])
            i+=1
        else:
            i+=1
    return lista_p
def filtra_positivos(lista):
    lista_positivos = []
    i = 0
    for i in range(len(lista)):
        if lista[i] > 0:
            lista_positivos.append(lista[i]) 
            i += 1
        else:
            i += 1
            continue
    return lista_positivos
def filtra_positivos(lista):
    i = 0
    while i<=len(lista):
        lista_positivos = []
        if lista[i] > 0:
            lista_positivos.append(lista[i]) 
            i += 1
        else:
            i += 1
            continue
    return lista_positivos
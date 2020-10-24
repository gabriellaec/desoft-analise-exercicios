def filtra_positivos(lista):
    contador = True
    lista_positivos = []
    i = 0
    while contador:
        if lista[i] > 0:
            lista_positivos.append(lista[i]) 
            i += 1
        else:
            i += 1
            continue
    return lista_positivos
def filtra_positivos(lista):
    contador = True
    lista_positivos = []
    i = 0
    while contador:
        if lista[i] > 0:
            lista_positivos.append(lista[i]) 
        else:
            continue
    return lista_positivos
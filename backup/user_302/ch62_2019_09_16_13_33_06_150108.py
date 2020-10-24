def filtra_positivos(lista):
    i = 0
    segunda_lista = []
    while i < len(lista):
        if lista[i] > 0:
            segunda_lista.append(lista[i])
        i += 1
    return segunda_lista
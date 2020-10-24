def filtra_positivos(lista):
    i = 0
    while i < len(lista):
        if lista[i] < 0:
            del lista[i]
        else:
            i += 1            
    return lista

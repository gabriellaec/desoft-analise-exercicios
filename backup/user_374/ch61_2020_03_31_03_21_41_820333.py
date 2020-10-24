def filtra_positivos(lista):
    i = 0
    if len(lista) == 1 and lista[0] < 0: 
        return 0
    else: 
        while i < len(lista):
                if lista[i] < 0:
                    del lista[i]
                i += 1
        return lista
def filtra_positivos(lista):
    x = 0
    lista_par = []
    while x < len(lista):
        if lista[x] >= 0:
            lista_par.append(lista[x])
    return lista_par
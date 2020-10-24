def filtra_positivos(lista):
    x = 0
    lista_par = []
    while x < len(lista):
        if lista[x] >= 0:
            lista_par.append(lista[x])
        x += 1
    return lista_par
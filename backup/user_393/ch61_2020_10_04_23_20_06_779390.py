def filtra_positivos(lista):
    lista_estritamente_positivos= []
    i= 0
    while i < len(lista):
        if lista[i] > 0:
            lista_estritamente_positivos.append(lista[i])
            i= i + 1
        else:
            i= i + 1
    return lista_estritamente_positivos
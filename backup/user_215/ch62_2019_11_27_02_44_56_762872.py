def filtra_positivos(lista):
    lista_nova = []
    for i in lista:
        if i > 0:
            lista_nova.append(i)
    return lista_nova
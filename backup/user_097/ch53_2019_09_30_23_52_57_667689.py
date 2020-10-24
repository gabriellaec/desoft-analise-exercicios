def inverte_lista(lista):
    lista_inversa = []
    i = len(lista)-1
    while (i >= 0):
        lista_inversa.append(lista[i])
        i = i - 1
    return lista_inversa
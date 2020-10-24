def inverte_lista(lista):
    listaInvertida = []
    indice = -1
    while len(listaInvertida) < len(lista):
        num = lista[indice]
        listaInvertida.append(num)
        indice -= 1
    return listaInvertida
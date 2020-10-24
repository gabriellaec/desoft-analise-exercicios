def equaliza_imagem(lista, k):
    indice = 0
    while indice < int(len(lista)):
        lista[indice] = lista[indice] * k
        if lista[indice] < 255:
            lista[indice] = 0
        indice = indice + 1
    return lista
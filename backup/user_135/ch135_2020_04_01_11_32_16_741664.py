def equaliza_imagem(lista, k):
    indice = 0
    while indice < int(len(lista)):
        lista[indice] = lista[indice] * k
        indice = indice + 1
        if lista[indice] < 255:
            lista[indice] = 255
    return lista
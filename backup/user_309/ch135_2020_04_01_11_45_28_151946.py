def equaliza_imagem(lista,k):
    for i in range(len(lista)):
        lista[i] *= k
        if lista[i]>255:
            lista[i] = 255
    return lista
        
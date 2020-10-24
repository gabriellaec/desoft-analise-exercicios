def equaliza_imagem(lista,k):
    while i<len(lista):
        lista[i] *= k
        if lista[i]>255:
            lista[i] = 255
    return lista
        
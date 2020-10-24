def equaliza_imagem(lista, k):
    a = len(lista)
    i = 0
    while a>i:
        lista[i]= k * lista[i]
        if lista[i]>255:
            lista[i]= 255
        i+=1
    return lista
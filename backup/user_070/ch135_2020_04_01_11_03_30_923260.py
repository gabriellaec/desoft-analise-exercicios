def equaliza_imagem(lista,k):
    n = len(lista)
    i = 0
    while i < n:
        lista[i] = lista[i] * k
        if lista[i] > 255:
            lista[i] = 255
        i += 1
    return lista
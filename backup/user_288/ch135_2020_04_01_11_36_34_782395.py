def equaliza_imagem (lista, k):
    i = 0
    while i < len(lista):
        lista[i] *= k
        elif lista[i] > 255:
            lista[i] = 255
             i += 1
        else:
             i += 1
    return lista
    
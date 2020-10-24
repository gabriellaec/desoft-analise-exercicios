
def equaliza_imagem(lista, k):
    i = 0
    while i < len(lista):
        lista[i] = lista[i] * k
        i += 1
    i = 0
    while i < len(lista):
        if lista[i] > 255:
            lista[i]= 255
        i += 1


    return lista
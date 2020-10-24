def equaliza_imagem(lista, k):
    final = [0]*len(lista)
    i=0
    while i < len(lista):
        if lista[i]*k < 255:
            final[i] = lista[i]*k
        else:
            final[i] = 255
        i+=1
    return final
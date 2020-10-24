def equaliza_imagem (lista, k):
    i= 0
    while i< int(len(lista)):
        lista[i]= lista[indice]*k
        if lista[i] > 255:
            lista[i] = 255
            i=i+1
    return lista
            

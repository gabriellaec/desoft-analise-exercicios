def equaliza_imagem(lista, k):
    m=0
    i=0
    if i<256 and i>=0:
        for i in range (0,256):
            m = lista[i]*k
        i=i+1
    return m 
        
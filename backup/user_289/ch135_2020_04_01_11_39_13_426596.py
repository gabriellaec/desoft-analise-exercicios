def equaliza_imagem(lista, K):
    i = 0
    lista=[0]*256
    lista[0]= 0
    i += 1
    
    int(K)
    nova_lista = lista*K
    if nova_lista[i] > 255:
        nova_lista[i] = 255
    return nova_lista
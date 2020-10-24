def equaliza_imagem (lista, k):
    i= 0    
    b=len(lista)    
    while (b>i):
        lista = lista[i]*k
        if lista[i] > lista[255]:
            lista[i] = 255
            i += 1
               
    return lista
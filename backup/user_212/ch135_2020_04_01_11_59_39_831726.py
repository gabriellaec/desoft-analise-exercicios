def equaliza_imagem (lista, k):
    i= 0    
    b=len(lista)
    lista = lista[:]*k
    while (b>i):
            if lista[i] > lista[255]:
                lista[i] = 255
                i += 1
            if lista[i] < lista[0]:
                lista[i] = 0
                i+=1                          
    return lista
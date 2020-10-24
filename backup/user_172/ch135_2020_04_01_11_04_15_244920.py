def equaliza_imagem (lista):
    k=1
    nova_lista=[]
    i=0
    x = len(lista)
    while i<len(lista):
        lista[i] = nova_lista[k*i]
        i+=1
        k+=1
        if k*i>255:
            k*i==255
            lista_nova.append(k*i)
    return nova_lista
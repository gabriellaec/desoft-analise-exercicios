def equaliza_imagem (lista):
    lista=[]
    k=1
    nova_lista=[]
    i=0
    x = len(lista)
    while i<len(lista)-1:
        lista[i] = nova_lista[k*i]
        i+=1
        if k*i>255:
            k*i==255
            nova_lista.append(k*i)
        k+=1
    return nova_lista
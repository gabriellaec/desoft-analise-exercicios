def equaliza_imagem (lista,k):
    lista=[]
    k=1
    nova_lista=[]
    i=0
    x = len(lista)
    while i<len(lista)-1:
        lista[i] = k*lista[i]
        i+=1
        nova_lista.append(k*lista[i])
        if k*lista[i]>255:
            k*lista[i]==255
            nova_lista.append(k*lista[i]) 
        k+=1       
    return nova_lista
def equaliza_imagem (lista,k):
    k=2
    nova_lista=[]
    i=0
    x = len(lista)
    while i<x:
        lista[i] = k*lista[i]
        if k*lista[i]>=255:
            k*lista[i]==255
            nova_lista.append(k*lista[i]) 
        nova_lista.append(k*lista[i])
        i+=1
        k=k+8     
    print (nova_lista)
    return nova_lista
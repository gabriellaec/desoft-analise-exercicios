def equaliza_imagem (lista,k):
    
    nova_lista=[]
    i=0
    x = len(lista)
    while i<x:
        k=2
        lista[i] = k*lista[i]
        if k*lista[i]>=255:
            k*lista[i]==255
            nova_lista.append(k*lista[i]) 
        nova_lista.append(k*lista[i])
        i+=1
    while i<x:
        k=10
        lista[i] = k*lista[i]
        if k*lista[i]>=255:
            k*lista[i]==255
            nova_lista.append(k*lista[i]) 
        nova_lista.append(k*lista[i])
        i+=1
    print (nova_lista)
    return nova_lista
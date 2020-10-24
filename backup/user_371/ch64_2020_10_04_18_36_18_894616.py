def acha_bigramas(palavra):
    i=0
    lista=[]
    while (len(palavra)-1)>i:
        lista.append(palavra[i]+palavra[i+1])
        i+=1
    i=0
    j=0
    lista_nova=lista
    while len(lista)>i: 
        while j<len(lista):
            if lista[i]==lista[j] and j!=i:
                del lista[j]
                j+=1
            else:
                j+=1
        i+=1
    return lista
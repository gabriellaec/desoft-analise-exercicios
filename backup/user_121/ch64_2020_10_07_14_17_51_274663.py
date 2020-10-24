def acha_bigramas(string):
    lista=[]
    i=1
    while i<len(string):
        lista.append(string[i-1]+string[i])
        i+=1
    i=0
    while i<len(lista):
        j=i
        while j<len(lista):
            if lista[i]==lista[j] and i!=j:
                del(lista[i])
            j+=1
        i+=1
    return lista
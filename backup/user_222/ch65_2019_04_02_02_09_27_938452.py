def acha_bigramas(palavra):
    lista_bigramas=[]
    i=1
    while i<len(palavra):
        if i%2==0:
            k=palavra[i-1].append(lista_bigramas)+palavra[i].append(lista_bigramas)
    i+=1
    return k
    
            
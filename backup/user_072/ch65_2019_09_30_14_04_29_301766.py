def acha_bigramas(string):
    bigrama=[]
    lista1=[]
    lista2=[]
    i=0
    while i<len(string)-1:
        lista1.append(string[i])
        lista2.append(string[i+1])
        x=lista1[i]+lista2[i]
        if x not in bigrama:
            bigrama.append(x)
        i+=1
    return bigrama
def acha_bigramas(x):
    i=0
    a=''
    lista=[]
    bigrama=[]
    while i<len(x):
        a=x[i:(i+2)]
        lista.append (a)
        i+=1
    i=0
    while i<len(lista):
        if len(lista[i])<2:
            del lista[i]
        i+=1
    i=0
    while i<len(lista):
        if lista[i] not in bigrama:
            bigrama.append (lista[i])
        i+=1
    return bigrama
def conta_bigramas(texto):
    lista= list(str(texto))
    i = 0
    silabas=[]
    dicionario={}
    
    while i < len(lista)-1:
        silaba = lista[i]+lista[i+1]
        silabas.append(silaba)
        i+=1
    for i in silabas:
        if i not in dicionario.keys():
            dicionario[i]=1
        else:
            n= dicionario[i]
            dicionario[i]=n+1
    return dicionario
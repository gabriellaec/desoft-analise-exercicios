def conta_bigramas(string):
    i=0
    dicionario={}
    lista=[]
    while i<len(string)-1:
        lista.append(string[i]+string[i+1])
        i+=1
    for e in lista:
        if e in dicionario:
            dicionario[e]+=1
        else:
            dicionario[e]=1
    return dicionario
    
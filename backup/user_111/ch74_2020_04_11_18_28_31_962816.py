def conta_bigramas(palavra):
    i=1
    dicionario={}
    while i<len(palavra):
        if (palavra[i-1]+palavra[i]) not in dicionario:
            dicionario[i-1]=1
        else:
            dicionario[i-1]+=1
        i+=1
    return dicionario
 
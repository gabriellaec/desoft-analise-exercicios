def conta_bigramas(palavra):
    dicionario={}
    for i in range(1,len(palavra)):
        soma=palavra[i-1]+palavra[i]
        if soma not in dicionario:
            dicionario[soma]=1
        else:
            dicionario[soma]+=1
    return dicionario
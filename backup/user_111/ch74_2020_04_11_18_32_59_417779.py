def conta_bigramas(palavra):
    dicionario={}
    for i in range(1,len(palavra)):
        if (palavra[i-1]+palavra[i]) not in dicionario:
            dicionario[palavra[i-1]+palavra[i]]=1
        else:
            dicionario[palavra[i-1]+palavra[i]]+=1
    return dicionario
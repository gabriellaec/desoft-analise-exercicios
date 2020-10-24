def conta_bigramas(palavra):
    dicionario={}
    for i in range(0,len(palavra),2):
        if i not in dicionario:
            dicionario[i]=1
        else:
            dicionario[i]+=1
    return dicionario
 
def conta_bigramas(texto):
    dicionario=dict()
    
    for i in range(len(texto)-1):
        bigrama= texto[i]+texto[i+1]
        
        if bigrama not in dic:
            dicionario[bigrama]=1
        else:
            dicionario[bigrama]+=1
    return dicionario
        
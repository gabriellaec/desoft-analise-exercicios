def conta_bigramas(palavra):
    dicionario = {}
    for i in range(len(palavra)-1):
        bigrama = palavra[i] + palavra[i+1]
        if bigrama not in dicionario:
            dicionario[bigrama]=1
        else:
            dicionario[bigrama]+=1
    return dicionario
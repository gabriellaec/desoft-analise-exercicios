def conta_bigramas(lista):
    dicionario=dict()
    for bigrama in lista:
        if not bigrama in dicionario:
            dicionario[bigrama]=1
        else:
            dicionario[bigrama]+=1
    return dicionario
        
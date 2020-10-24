def conta_bigramas(texto):
    dicionario=dict()
    for bigrama in texto:
        if not bigrama in dicionario:
            dicionario[bigrama]=1
        else:
            dicionario[bigrama]+=1
    return dicionario
        
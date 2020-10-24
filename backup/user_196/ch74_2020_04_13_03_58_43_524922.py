def conta_bigramas(a):
    dicionario = {}
    for bigrama in a:
        if bigrama in dicionario.keys():
            dicionario[bigrama]+=1
        else:
            dicionario[bigrama]=1
    return dicionario
   
def conta_bigramas(palavra):
    bigramo=acha_bigramos(palavra)
    dicionario = dict()
    i=0
    while i < len(bigramo):
        if bigramo[i] in dicionario:
            dicionario[bigramo[i]]+=1
        else:
            dicionario[bigramo[i]]=1
        i+=1
    return dicionario
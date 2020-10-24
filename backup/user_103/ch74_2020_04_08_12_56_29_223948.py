def conta_bigramas(palavra):
    dicionario={}
    for par in palavra:
        if not par in dicionario:
            dicionario[par]=1
        else:
            dicionario[par]+=1
        print (dicionario)
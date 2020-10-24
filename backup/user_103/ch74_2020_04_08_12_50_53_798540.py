def conta_bigramas(palavra):
    dicionario={}
    for par in palavra:
        if not par in dicionario:
            dicionario[par]=2
        else:
            dicionario[par]+=2
        print (dicionario)
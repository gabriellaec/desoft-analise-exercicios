def conta_letras(''):
    dicionario={}
    for t in len(''):
        if t in dicionario:
            dicionario[t]+=1
        else:
            dicionario[t]=1
    return dicionario
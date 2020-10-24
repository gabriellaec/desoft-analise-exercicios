def conta_letras(palavra):
    dicionario={}
    for t in palavra:
        if t in dicionario:
            dicionario[t]+=1
        else:
            dicionario[t]=1
    return dicionario
def mais_frequente(lista):
    dicionario={}
    for t in lista:
        if t in dicionario:
            dicionario[t]+=1
        else:
            dicionario[t]=1
    return dicionario.values:
        
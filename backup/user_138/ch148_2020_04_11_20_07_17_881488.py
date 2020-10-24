def conta_letras(string):
    dicionario={}
    for a in string:
        if a not in dicionario:
            dicionario[a]=1
        else:
            dicionario[a]+=1
    return dicionario
def conta_letras(string):
    dicionario={}
    for i in string:
        if i not in dicionario:
            dicionario[i]=1
        else:
            dicionario[i]+=1

    return dicionario
def conta_letras(palavra):
    dicionario={}
    for i in palavra:
        if i not in dicionario:
            dicionario[i]=1
        else:
            dicionario[i]+=1
    return dicionario
            
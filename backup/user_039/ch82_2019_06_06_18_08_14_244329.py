def primeiras_ocorrencias(palavra):
    dicionario={}
    for i in palavra:
        if i not in dicionario:
            dicionario[i]=0
        else:
            dicionario[i]+=1
    return dicionario
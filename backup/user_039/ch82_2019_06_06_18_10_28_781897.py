def primeiras_ocorrencias(palavra):
    dicionario={}
    a=-1
    for i in palavra:
        a+=1
        if i not in dicionario:
            dicionario[i]=a
    return dicionario
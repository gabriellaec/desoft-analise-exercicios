def primeiras_ocorrencias(palavra):
    dicionario={}
    cont=0
    for i in palavra:
        dicionario[i]=cont
        cont+=1
    return dicionario
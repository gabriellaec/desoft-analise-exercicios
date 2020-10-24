def primeiras_ocorrencias(palavra):
    dicionario={}
    cont=0
    for i in len(palavra):
        dicionario[palavra[i]]=cont
        cont+=1
    return dicionario
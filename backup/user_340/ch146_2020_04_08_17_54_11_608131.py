def  conta_ocorrencias(lista):
    dicionario={}
    for t in lista:
        dicionario[t]=1
    if dicionario[t] in dicionario:
        dicionario[t]+=1
    return dicionario
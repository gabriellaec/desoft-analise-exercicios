def  primeiras_ocorrencias(palavra):
    dicionario={}
    i=0
    for t in palavra:
        dicionario[t]=i
        i+=1
        if t in dicionario:
            dicionario[t]=dicionario[t]
    return dicionario
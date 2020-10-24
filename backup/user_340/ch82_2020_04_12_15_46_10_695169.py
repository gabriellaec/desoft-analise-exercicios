def  primeiras_ocorrencias(palavra):
    dicionario={}
    i=0
    for t in palavra:
        if not t in dicionario:
            dicionario[t]=i
            i+=1
    return dicionario
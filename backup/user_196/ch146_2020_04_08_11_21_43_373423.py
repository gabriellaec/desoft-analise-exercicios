def conta_ocorrencias(a):
    dicionario{}
    for palavra in a.keys():
        if palavra in dicionario:
            dicionario[palavra]+=1
        else:
            dicionario[palavra] = 1
    return dicionario
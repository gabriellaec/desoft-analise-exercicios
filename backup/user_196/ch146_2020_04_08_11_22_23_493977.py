def conta_ocorrencias(a):
    dicionario{}
    for palavra in a:
        if palavra in dicionario.keys():
            dicionario[palavra]+=1
        else:
            dicionario[palavra] = 1
    return dicionario